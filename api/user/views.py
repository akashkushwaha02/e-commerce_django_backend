from django.shortcuts import render

from django.contrib.auth import login, logout
from rest_framework import serializers
from  rest_framework.permissions import AllowAny
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import viewsets
import random
# Create your views here.


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(length)]) for _ in range(length))

@csrf_exempt
def signin(request):    
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a POST request with valid parameters'})
    
    username = request.POST['email']
    password = request.POST['password']

    #validation part
    if not re.match("^\S+@\S+$",username):
        return JsonResponse({'error':'Enter a valid email'})
    if len(password) < 3:
        return JsonResponse({'error':'password needs to be atleast length 3'})

    userModel = get_user_model()
    
    try:
        user = userModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = userModel.objects.filter(email=username).values().first()

            if user.session_token !="0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'Previous session exists!'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request,user)
            return JsonResponse({'token': token,'user':usr_dict})
        else:
            return JsonResponse({'error':'Invalid password'})
    except userModel.DoesNotExist:
        return JsonResponse({'error':'Invalid email'})


def signout(request,id):
    logout(request)

    userModel = get_user_model()

    try:
        user = userModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except userModel.DoesNotExist:
        return JsonResponse({'error': 'something went wrong or invalide user id'})

    return JsonResponse({'success':'Logout successful'})



class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create':[AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action ]]
        except KeyError:
            return [permission() for permission in self.permission_classes]