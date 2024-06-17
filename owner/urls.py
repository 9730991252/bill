from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard,name='owner_dashboard'),   
    path('item_name/', views.item_name,name='item_name'),      
    path('add_stock/', views.add_stock,name='add_stock'),   
    path('sell_item/', views.sell_item,name='sell_item'),   
    path('profile/', views.profile,name='profile'),   
    path('complate_view_order/<int:id>', views.complate_view_order,name='complate_view_order'),   
    path('complate_bill/', views.complate_bill,name='complate_bill'),   
  
]  