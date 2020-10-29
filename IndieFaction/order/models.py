from django.db import models
import uuid
from colledition.models import CollectorEdition
from accounts.models import UserName, Address
from django.core.validators import RegexValidator


class Order(UserName, Address):
    order_id = models.UUIDField(
        default=uuid.uuid4, verbose_name='order_id', primary_key=True, editable=False)
    contact_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_no = models.CharField(
        validators=[contact_regex], max_length=17, blank=False)
    token = models.CharField(
        max_length=50, verbose_name='Token', default='#T', unique=True)
    status = models.CharField(
        max_length=50, verbose_name='Status', default='NA', editable=False)
    cid = models.ForeignKey(CollectorEdition, verbose_name=(
        "cid"), on_delete=models.CASCADE)

    def __str__(self):
        return self.cid.name+" "+self.status

    class Meta:
        abstract = True


class PrintOrder(Order):
    pass


class CompletedOrder(Order):
    pass
