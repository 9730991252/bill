from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard,name='owner_dashboard'),   
    path('item/', views.item,name='item'),    
    path('stock_item_filter/', views.stock_item_filter,name='stock_item_filter'),   
    path('add_stock/', views.add_stock,name='add_stock'),   
    path('sell_item/', views.sell_item,name='sell_item'),   
    path('complate_view_order/<int:id>', views.complate_view_order,name='complate_view_order'),   
    path('complate_bill/', views.complate_bill,name='complate_bill'),   
  
] 