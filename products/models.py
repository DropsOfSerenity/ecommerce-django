from django.db import models
from django.core.urlresolvers import reverse

optional = {'null': True, 'blank': True}


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        abstract = True


class Product(TimestampedModel):
    title = models.CharField(max_length=120)
    description = models.TextField(**optional)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, **optional)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})
    
    def has_featured_image(self):
        return bool(self.productimage_set.filter(featured=True))
    
    def get_featured_image(self):
        return self.productimage_set.filter(featured=True).first()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        unique_together = ('title', 'slug')


class ProductImage(TimestampedModel):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.product.title
