from django.urls import path, re_path
from .views import (
	ListPage,
	DetailPage,
	create_cart,
	SearchResultsView,
	# OrderSummaryView,
	delete_item,
	clear,
	SummaPage,
)
from django.contrib.auth.decorators import login_required
app_name = 'core'

urlpatterns = [
	path('create-cart/<slug>/', login_required(create_cart), name='create-cart'),
	path('summary/', login_required(SummaPage), name='summary'),
	re_path('search/', SearchResultsView.as_view(), name='search-results'),
	path('clear/', clear, name='clear'),
	path('delete-item/<slug>/', delete_item, name='delete-item'),
	path('<slug>/', DetailPage.as_view(), name='detail-product'),
	path('', ListPage.as_view(), name='list-product'),
]
