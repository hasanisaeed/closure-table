from django.contrib.auth.models import User
from django.db import models
from core.model.closure_table import ClosureModel


class AccountGroup(models.Model):
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='account_groups')
    title = models.CharField(max_length=50)
    coding = models.PositiveSmallIntegerField(null=False, blank=False)


class AccountGeneral(models.Model):
    account_group = models.ForeignKey(AccountGroup, on_delete=models.PROTECT, related_name='account_generals')
    title = models.CharField(max_length=50)
    coding = models.PositiveSmallIntegerField(null=False, blank=False)


class AccountSubsidiary(models.Model):
    account_general = models.ForeignKey(AccountGeneral, on_delete=models.PROTECT, related_name='account_subsidiaries')
    title = models.CharField(max_length=100)
    # Includes all parent codings.
    coding = models.PositiveIntegerField(null=True, blank=True)


class AccountDetail(ClosureModel):
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='children',
                               null=True,
                               blank=True)

    account_subsidiary = models.ForeignKey(AccountSubsidiary,
                                           on_delete=models.PROTECT,
                                           related_name='account_details')

    coding = models.PositiveBigIntegerField(null=True, blank=True)

    class ClosureMeta(object):
        """Closure options."""
        parent_attr = "parent"

    def __repr__(self):
        return self.coding
