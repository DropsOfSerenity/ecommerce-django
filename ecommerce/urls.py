from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from products import urls as products_urls

urlpatterns = [
    url(r'^$', 'products.views.home', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),

    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.update_cart',
        name='update_cart'),

    url(r'^products/', include(products_urls, namespace='products')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
