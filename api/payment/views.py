from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree

# Create your views here.


gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='gf4p7y9qcsk6wqs6',
    public_key='k7vmkpb8kxd7fxft',
    private_key='1111ce7abd201f11129d45f2c6dd989e'
  )
)

def validate_session_token(id,token):
    userModel = get_user_model()

    try:
        user = userModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except userModel.DoesNotExist:
        return False

@csrf_exempt
def generate_token(request,id,token):
    if not validate_session_token(id,token):
        return JsonResponse({'error':'Invalid session,Please login again'})

    return JsonResponse({'clientToken':gateway.client_token.generate(),'success':'session geenrated succesfully'}
    )