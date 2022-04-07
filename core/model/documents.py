from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels

from core.model import AccountSubsidiary, AccountDetail


class DocumentHead(models.Model):
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='document_heads')
    content = models.CharField(max_length=200, null=True, blank=True)
    number = models.PositiveIntegerField(null=False, blank=False)
    date = jmodels.jDateField()

    def __str__(self):
        return f'{self.date.strftime("%Y/%m/%d")} - {self.number}'


class DocumentDetail(models.Model):
    document_head = models.ForeignKey(DocumentHead, on_delete=models.PROTECT, related_name='document_details')
    content = models.CharField(max_length=200, null=True, blank=True)
    price = models.BigIntegerField(null=False, blank=False)
    cost_center = models.CharField(max_length=20, null=True, blank=True)
    account_subsidiary = models.ForeignKey(AccountSubsidiary, null=True, blank=True, on_delete=models.PROTECT,
                                           related_name='document_details')
    account_detail = models.ForeignKey(AccountDetail, null=True, blank=True, on_delete=models.PROTECT,
                                       related_name='document_details')
    # account_detail_level_two = models.ForeignKey(AccountDetailLevelTwo, null=True, blank=True, on_delete=models.PROTECT,
    #                                              related_name='document_details')

    def __str__(self):
        return f'{self.price} : {self.content}'
