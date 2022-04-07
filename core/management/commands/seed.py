from django.core.management.base import BaseCommand

from core.models import A


def populate_A():
    a1 = A.objects.create(name='A')

    a2 = A.objects.create(name='B')
    a2.parent2 = a1

    a3 = A.objects.create(name='C')
    a3.parent2 = a1

    a4 = A.objects.create(name='D')
    a4.parent2 = a1


def get_A():
    a = A.objects.filter(name='B').first()
    print(a.get_descendants(include_self=True))
    print(a.get_ancestors(include_self=True))


def test_ancestor():
    a = A.objects.create(name="a")
    b = A.objects.create(name="b")
    c = A.objects.create(name="c")
    b.parent2 = a
    b.save()
    c.parent2 = b
    c.save()

    # Testing the ancestors method
    print(list(a.get_ancestors()))
    print(list(b.get_ancestors(include_self=True)))
    print(list(a.get_ancestors(include_self=True)))
    print(list(c.get_ancestors(include_self=True)))
    print()
    print(list(c.get_ancestors(include_self=True, depth=0)))
    print(list(c.get_ancestors(include_self=True, depth=1)))
    print(list(c.get_ancestors(include_self=True, depth=2)))


class Command(BaseCommand):

    def handle(self, *args, **options):
        # populate_A()
        # get_A()
        test_ancestor()
