from django.urls import path
from ajax import views
urlpatterns = [
    path('add_to_cart/', views.add_to_cart,name='add_to_cart'), 
    path('customer_filter/', views.customer_filter,name='customer_filter'), 
    path('new_item_filter/', views.new_item_filter,name='new_item_filter'),  
    path('sell_item_filter/', views.sell_item_filter,name='sell_item_filter'),  
]