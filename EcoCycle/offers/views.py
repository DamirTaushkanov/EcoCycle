from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from offers.models import Offers
from items.models import Products

@login_required
def create_offer_web(request):
    if request.method == 'POST':
        try:
            sender_product = Products.objects.get(id=request.POST.get('sender_product_id'), user_id=request.user)
            addressee_product = Products.objects.get(id=request.POST.get('addressee_product_id'))
            # Создаем предложение обмена
            offer = Offers.objects.create()
            offer.sender_item.add(sender_product)
            offer.addressee_products.add(addressee_product)
            offer.save()

            return JsonResponse({"status": "success", "message": "Offer created successfully"})
        except Products.DoesNotExist:
            return JsonResponse({"status": "error", "message": "One or both products do not exist"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=400)
