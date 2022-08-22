
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.users),
    path('user/<int:pk>/', views.user),
    path('signin/', views.signin),
    path('signup/', views.signup),

]



