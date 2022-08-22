from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
import random
from django.shortcuts import get_object_or_404
from decimal import Decimal


@api_view(["GET", ])  
def foods(request):
    foods = Food.objects.filter()
    
    if foods is None:
        return Response({"error":"No food found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FoodSerializer(foods, many = True, context = {'request':request})
    return Response({"foods":serializer.data}, status=status.HTTP_200_OK)


@api_view(["PUT",  "GET", "DELETE",])  
def food(request, pk):
    pass


@api_view(["POST",  "GET",])  
def orders(request):
    if request.method == "GET":
        orders = Order.objects.filter()
    
        if orders is None:
            return Response({"error":"No order found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FoodSerializer(foods, many = True, context = {'request':request})
        return Response({"orders":serializer.data}, status=status.HTTP_200_OK)

    if request.method == "POST":
        pass



@api_view(["PUT",  "GET", "DELETE",])  
def order(request, pk):
    pass