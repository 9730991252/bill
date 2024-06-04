from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us/', views.contact_us,name='contact_us'),
    path('woner_logout/', views.woner_logout,name='woner_logout'),
]