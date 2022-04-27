
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.urls import re_path as url

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pay/', include('pay.urls')),
    path('api/v1/', include(('api_product.urls', 'api-product'), namespace='api-product')),
    path('api/v1/accounts/', include(('api_accounts.urls', 'api-accounts'), namespace='api-accounts')),
    path('', include(('product.urls', 'product'), namespace='product')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

