
from django.urls import path
from . import views


urlpatterns = [
    path('foods/', views.foods),
    path('food/<int:pk>/', views.food),
    path('orders/', views.orders),
    path('order/<int:pk>/', views.order),

]



