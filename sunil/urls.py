from django.urls import path
from sunil import views
urlpatterns = [
    path('sunil_dashboard/', views.sunil_dashboard,name='sunil_dashboard'),    
    path('add_medical/', views.add_medical,name='add_medical'),    
]