
from django.urls import path
from store import views

app_name='store'
urlpatterns = [
    path('',views.HomeView.as_view(), name='Store'),
    path('product/<int:pk>/',views.product_details, name='product')
    
]