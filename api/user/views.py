from django.shortcuts import render
import random
from django.contrib.auth import login, logout
from rest_framework import serializers
from  rest_framework.permissions import AllowAny
import re
from django.http import JsonResponse
from django.view.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr[i] for i in range(97,123)] + [str(i) for i in range(length)]) for _ in range(length))

@csrf_exempt
def signup(request):
    