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


# Create your views here.


@api_view(["POST"])
@permission_classes((AllowAny,))
def signin(request):   

    email = request.data.get("email", None)
    password = request.data.get("password", None) 

    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                       status=status.HTTP_400_BAD_REQUEST)      
    
    # Authenticate user using django contrib in-built authenticate
    user = authenticate(request, username=email, password=password)   
       
            
    if user:        
        if user.is_active:    
                 
            login(request, user)
                        
            token, _ = Token.objects.get_or_create(user=user)

            dashboard = {}
            dashboard["user"] = user
            dashboard["token"] = token
                          
             
            serializer = DashboardSerializer(dashboard, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)                                 

        else:             
            return Response({'error': "There is a problem with your account. Please contact support for details"}, 
                             status=status.HTTP_403_FORBIDDEN)      
           
    else:        
        return Response({'error': "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
        
        

@api_view(["POST",])
@permission_classes((AllowAny,))
def  signup (request):

    fullname = request.data.get("fullname").split(" ", 1)
    first_name = fullname[0]
    last_name = fullname[1]
    
    
    user = UserSerializer(data= {         
         'first_name':first_name,
         'last_name': last_name,
         'phone': request.data.get("phone"),
         'email':request.data.get("email"),         
         'password':make_password(request.data.get('password')),
         'username':make_username(first_name),
        
                 
    })



    if user.is_valid():                 
        u = user.save()
        token = Token.objects.create(user=u)
 
        return Response(
                {'message': 'Account creation was successful.'},
                    status.HTTP_201_CREATED
            ) 
        
    else:
        
    
        return Response({"error": user.errors }, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(["PUT",  "GET", "DELETE",])  
def user(request, pk=None):
    
    user = get_object_or_404(User, pk=pk)
    
    #profile screen
    if request.method == "GET":        
        
        serializer = UserSerializer(user, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)                                 
    
    #delete user - admin action or self action
    if request.method == "DELETE":
        user.delete()
        return Response({"message":"User deleted"}, status=status.HTTP_204_NO_CONTENT)


    #edit profile - self action
    if request.method == "PUT":
        user  = User.objects.get(pk=pk)
        
        first_name = request.POST.get('first_name', None)        
        last_name = request.POST.get('last_name', None)
        username = request.POST.get('username', None)         
        address = request.POST.get('country', None) 
        photo = request.FILES.get('photo', None)  
        
        if first_name != None:
            user.first_name = first_name

        if last_name != None:
            user.last_name = last_name

        if username != None:
            user.username = username
        
        if address != None:
            user.address = address

        if user.photo != None:
            user.photo = photo

        try:

            user.save()
            edited_user = User.objects.get(pk=pk)
            serializer = UserSerializer(edited_user, context = {'request':request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({"message":e.detail}, status=status.HTTP_304_NOT_MODIFIED)
  
                       
@api_view(["GET",])
def users(request):
    
    users = User.objects.filter(account_status="1", is_private=False, currency=request.user.currency).exclude(pk=request.user.id)
    
    if users is None:
        return Response({"error":"No user found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(users, many = True, context = {'request':request})
    return Response({"users":serializer.data}, status=status.HTTP_200_OK)




def make_username(first_name):
    random_figure = random.randint(100,200)    
    return first_name[:10]  + str(random_figure)