
from django.urls import path

from django.conf.urls import include
from django.urls import re_path as url

from api_product import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('create-cart/<slug>/', views.CreateCart.as_view(), name='api-create-cart'),
	path('clear/', views.ClearCart.as_view(), name='api-clear'),
	path('delete-by-id/<int:id>', views.Delete_By_Id.as_view(), name='api-delete-by-id'),
	path('list/', views.ListProduct.as_view() , name='api-list'),
	path('detail/<slug>/', views.DetailProduct.as_view(), name='api-show'),
	path('summary/', views.SummaPage.as_view(), name='api-summary'),
]