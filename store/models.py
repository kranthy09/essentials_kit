from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, timedelta

from django.db.models.query_utils import select_related_descend


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=100)

class Form(models.Model):

    LIVE = 'LIVE'
    CLOSED = 'CLOSED'
    DONE = 'DONE'
    INACTIVE = 'INACTIVE'
    FORM_STATUS = (
        (LIVE, 'Live'),
        (CLOSED, 'Closed'),
        (DONE, 'Done'),
        (INACTIVE, 'Inactive')
    )

    form_name = models.CharField(max_length=20)
    form_status = models.CharField(
        max_length=9,
        choices=FORM_STATUS,
        default='INACTIVE'
    )
    form_instructions = models.CharField(
        max_length=200,
        default="instructions"
    )
    available_till = models.DateTimeField(
        default=str(datetime.now() + timedelta(days=30))
    )

class UserForm(models.Model):
    user = models.ForeignKey(
        User,
        related_name='users',
        on_delete=models.CASCADE
    )
    form = models.ForeignKey(
        Form,
        related_name='forms',
        on_delete=models.CASCADE
    )
    user_form_updates = models.CharField(max_length=50)

class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

    def __str__(self):
        return 'brand: {}'.format(self.brand_name)

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_description = models.CharField(
        max_length=200,
        default="item_description"
        )
    brands = models.ManyToManyField(
        Brand,
        through="ItemBrand",
        through_fields=['item', 'brand']
    )
    item_category = models.CharField(max_length=9, default="CATEGORY")

class ItemBrand(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )
    quantity_available = models.IntegerField()
    price = models.DecimalField(
        max_digits=9,
        decimal_places=3,
    )

class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )
    quantity_ordered = models.IntegerField(default=0)
    quantity_delivered = models.IntegerField(blank=True, null=True, default=0)
