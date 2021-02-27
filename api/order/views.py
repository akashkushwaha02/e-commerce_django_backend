from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def validate_user_session(id,token):
    userModel = get_user_model()

    try:
        user == userModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except userModel.DoesNotExist:
        return False


@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Please login ','code':'1'})
    
    if request.method == 'POST':
        user_id = id 
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        product = request.POST['products']
        
        total_pro = len(product).split(',')[:-1]

        userModel = get_user_model()

        try:
            usr = userModel.objects.get(pk=user_id)
        except userModel.DoesNotExist:
            return JsonResponse({'error': 'user does not exist'})

        ordr = Order(user=usr,product_names=products,total_product=total_pro,transaction_id=transaction_id,total_amount=amount)
        ordr.save()

        return JsonResponse({'success':True,'error':False,'msg':'Order misplaced'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

    
