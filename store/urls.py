
from django.urls import path
from store import views

app_name='store'
urlpatterns = [
  
    path('',views.Store, name='Store')
    
]