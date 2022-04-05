from django.db import models


class Page(models.Model):
    path = models.CharField(max_length=100, blank=False, primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('rank',)


class Edge(models.Model):
    # Closure Table Tree Implementation
    # see: https://pragprog.com/book/bksqla/sql-antipatterns
    left = models.ForeignKey(Page,
                             related_name="parents",
                             blank=False,
                             on_delete=models.CASCADE
                             )
    right = models.ForeignKey(Page,
                              related_name="children",
                              blank=False,
                              on_delete=models.CASCADE
                              )
    depth = models.IntegerField(blank=False)

    class Meta:
        unique_together = (('left', 'right'))

    def __repr__(self):
        return "<Edge: %s - %s (%s)>" % (
            self.left, self.right, self.depth)

    def __str__(self):
        return self.__repr__()


class Tree():

    def node(self, model):
        '''In the tree, each node points at itself'''
        Edge.objects.create(left=model, right=model, depth=0)

    def __contains__(self, model):
        try:
            Edge.objects.get(left=model, right=model, depth=0)
            return True
        except Edge.DoesNotExist:
            return False

    def _ensure_nodes(self, nodes):
        for node in nodes:
            if not node in self:
                self.node(node)

    def edge(self, parent, child):
        '''
        Creates an edge between two nodes.
        An edge connects an element to EACH of its child elements. The depth
        column can be used to query this relationship.
              1         Depth 0: (1,1), (2,2), (3,3) ...
            /   \       Depth 1: (1,2), (1,3), (2,4), (2,5), (3,6), (3,7)
           2     3      Depth 2: (1,4), (1,5), (1,6), (1,7)
          / \   / \     Depth 3: ...
         4   5 6   7
        Nodes are depth 0,
        Children/Parents are depth 1,
        All others (depth > 1) are descendants or ancestors
        '''

        self._ensure_nodes((parent, child))

        for edge in Edge.objects.filter(right=parent):
            Edge.objects.create(
                left=edge.left,
                right=child,
                depth=edge.depth + 1
            )

    def children(self, parent):
        return (e.right for e in Edge.objects.filter(left=parent, depth=1))
