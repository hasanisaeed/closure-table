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
    parent2 = models.ForeignKey('self',
                                on_delete=models.CASCADE,
                                related_name='children',
                                null=True,
                                blank=True)

    account_subsidiary = models.ForeignKey(AccountSubsidiary,
                                           on_delete=models.PROTECT,
                                           related_name='account_details')

    # Includes all parent codings.
    coding = models.PositiveBigIntegerField(null=True, blank=True)

    # detail_person = models.ForeignKey('DetailPerson', null=True, blank=True, on_delete=models.PROTECT,
    #                                   related_name='account_details')
    # detail_bank = models.ForeignKey('DetailBank', null=True, blank=True, on_delete=models.PROTECT,
    #                                 related_name='account_details')
    # detail_expenditure = models.ForeignKey('DetailExpenditure', null=True, blank=True, on_delete=models.PROTECT,
    #                                        related_name='account_details')
    # detail_other = models.ForeignKey('DetailOther', null=True, blank=True, on_delete=models.PROTECT,
    #                                  related_name='account_details')

    class ClosureMeta(object):
        """Closure options."""
        parent_attr = "parent"

    def __repr__(self):
        return self.coding

# class B(models.Model):
#     """A test model for foreign keys"""
#     b_name = models.CharField(max_length=32)
#
#
# class AccountDetail(models.Model):
#     account_subsidiary = models.ForeignKey(AccountSubsidiary, on_delete=models.PROTECT, related_name='account_details')
#     # Includes all parent codings.
#     coding = models.PositiveBigIntegerField(null=True, blank=True)
#     detail_person = models.ForeignKey('DetailPerson', null=True, blank=True, on_delete=models.PROTECT,
#                                       related_name='account_details')
#     detail_bank = models.ForeignKey('DetailBank', null=True, blank=True, on_delete=models.PROTECT,
#                                     related_name='account_details')
#     detail_expenditure = models.ForeignKey('DetailExpenditure', null=True, blank=True, on_delete=models.PROTECT,
#                                            related_name='account_details')
#     detail_other = models.ForeignKey('DetailOther', null=True, blank=True, on_delete=models.PROTECT,
#                                      related_name='account_details')


# class AccountDetailLevelTwo(models.Model):
#     account_detail = models.ForeignKey(AccountDetail, on_delete=models.PROTECT,
#                                        related_name='account_details_level_two')
#     # Includes all parent codings.
#     coding = models.PositiveBigIntegerField(null=True, blank=True)
#     detail_person = models.ForeignKey('DetailPerson', null=True, blank=True, on_delete=models.PROTECT,
#                                       related_name='account_details_level_two')
#     detail_bank = models.ForeignKey('DetailBank', null=True, blank=True, on_delete=models.PROTECT,
#                                     related_name='account_details_level_two')
#     detail_expenditure = models.ForeignKey('DetailExpenditure', null=True, blank=True, on_delete=models.PROTECT,
#                                            related_name='account_details_level_two')
#     detail_other = models.ForeignKey('DetailOther', null=True, blank=True, on_delete=models.PROTECT,
#                                      related_name='account_details_level_two')
