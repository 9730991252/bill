from django.urls import path
from ajax import views
urlpatterns = [
    path('add_to_cart/', views.add_to_cart,name='add_to_cart'), 
    path('customer_filter/', views.customer_filter,name='customer_filter'), 
    path('doctor_filter/', views.doctor_filter,name='doctor_filter'), 
    path('new_item_filter/', views.new_item_filter,name='new_item_filter'),  
    path('sell_item_filter/', views.sell_item_filter,name='sell_item_filter'),  
    path('invice_filter/', views.invice_filter,name='invice_filter'),  
    path('remove_cart/', views.remove_cart,name='remove_cart'),  
    path('add_stock_item_filter/', views.add_stock_item_filter,name='add_stock_item_filter'),  
] 