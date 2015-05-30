from django.db import models
from products.models import Product
from base.models import optional, TimestampedModel


class Cart(TimestampedModel):
    products = models.ManyToManyField(Product, **optional)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)
