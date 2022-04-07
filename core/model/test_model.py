from django.db import models

from core.model.closure_table import ClosureModel


class A(ClosureModel):
    """A test model."""
    parent2 = models.ForeignKey("self",
                                on_delete=models.CASCADE,
                                related_name="children",
                                null=True,
                                blank=True
                                )
    name = models.CharField(max_length=32)
    b = models.ForeignKey("B", on_delete=models.CASCADE, related_name="aaa", null=True, blank=True)

    class ClosureMeta(object):
        """Closure options."""
        parent_attr = "parent2"

    def __unicode__(self):
        return "%s: %s" % (self.pk, self.name)

    def __repr__(self):
        return self.name


class B(models.Model):
    """A test model for foreign keys"""
    b_name = models.CharField(max_length=32)
