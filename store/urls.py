
from django.urls import path
from store import views

app_name='store'
urlpatterns = [
    path('',views.HomeView.as_view(), name='Store'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product-details'),
    
]