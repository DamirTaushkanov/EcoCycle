import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from items.forms import ProductsForm, ProductImagesForm
from items.models import ProductImages, Products
from django.utils.timezone import now, timedelta


@login_required
def create_product_web(request):
    if request.method == 'POST':
        product_form = ProductsForm(request.POST)
        image_form = ProductImagesForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            try:
                product = Products.objects.create(
                    user_id=request.user,
                    title=product_form.cleaned_data['title'],
                    description=product_form.cleaned_data['description'],
                    categories=product_form.cleaned_data['count'],
                    count=product_form.cleaned_data['count'],
                )
                images = request.FILES.getlist('images')
                for image in images:
                    ProductImages.objects.create(product=product, images=image)
                return redirect('products_list')
            except Exception as e:
                return JsonResponse(str(e), status=400)

    else:
        product_form = ProductsForm()
        image_form = ProductImagesForm()

    return render(request, 'items/add_product.html', {
        'products_form': product_form,
        'product_images_form': image_form,
    })


@login_required
def products_list_web(request):
    products = Products.objects.all()
    return render(request, 'items/products_list.html', {'products': products})

@login_required
def delete_product_web(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Пытаемся найти продукт, принадлежащий текущему пользователю
            product = get_object_or_404(Products, product_id=data.get('productId'), user_id=request.user)
            print(product)
            product.delete()
            return JsonResponse({"status": "success", 'message': "Product deleted successfully"})
        except Products.DoesNotExist:
            return JsonResponse({"status": "error", 'message': "Product does not exist or you do not have permission to delete it."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", 'message': f"An unexpected error occurred: {str(e)}"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)


@login_required
def products_feed_web(request):
    try:
        # Дата за последние 7 дней
        last_week = now() - timedelta(days=7)

        # Фильтрация по категории или получение всех за последние 7 дней
        if request.POST.get('category'):
            products = Products.objects.filter(
                categories=request.POST.get('category'),
                date_added__gte=last_week
            ).order_by('-date_added')[:10]
        else:
            products = Products.objects.filter(
                date_added__gte=last_week
            ).order_by('-date_added')[:10]
        products = [
            {
                'id': product.product_id,
                'title': product.title,
                'category': product.categories,
                'price': product.price,
                'date_added': product.date_added,
                'description': product.description,
                'images': [image.images.url for image in product.images.all()]
            }
            for product in products
        ]
        return render(request, 'items/products_feed.html', {'products': products})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

