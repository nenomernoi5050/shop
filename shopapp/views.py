from django.http import Http404
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart

def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    clothing_product = CardProduct.objects.filter(subcategory__name_slug='clothing').order_by('?')[:4]
    socks_product = CardProduct.objects.filter(subcategory__name_slug='socks').order_by('?')[:4]
    prettyIncuffs_product = CardProduct.objects.filter(subcategory__name_slug='prettyIncuffs').order_by('?')[:4]

    context = {'cartItems': cartItems, 'items': items, 'order': order, 'prettyIncuffs_product': prettyIncuffs_product, 'clothing_product': clothing_product, 'socks_product': socks_product }

    return render(request, 'shopapp/home.html', context)


def catalog(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    object_list = CardProduct.objects.filter(subcategory__name_slug='clothing').order_by('?')
    cat = {'name_slug': 'clothing'}
    paginator = Paginator(object_list, 15)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {'posts': posts, 'cartItems': cartItems, 'items': items, 'order': order, 'cat': cat}
    return render(request, 'shopapp/product_list.html', context)


def product_detail(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']


    x = kwargs.get("slug")


    try:
        product = get_object_or_404(CardProduct, slug=x)
    except CardProduct.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    if product.size:
        size = product.size.split(',')
    else:
        size = ''
    context = {'product': product, 'size': size, 'cartItems': cartItems, 'items': items, 'order': order}

    return render(request, 'shopapp/product_detail.html', context)


def subcat(request, *args, ** kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']


    x = kwargs.get("slug")

    try:
        sub_cat = CardProduct.objects.filter(subcategory__name_slug=x)
        cat = get_object_or_404(Category, subcategory__name_slug=x)
    except Category.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    paginator = Paginator(sub_cat, 15)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {'posts': posts, 'x': x, 'cat': cat, 'cartItems': cartItems, 'items': items, 'order': order}
    return render(request, 'shopapp/product_list.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items': items, 'order': order,  'cartItems': cartItems}
    return render(request, 'shopapp/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shopapp/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    if not request.user.is_authenticated:
        return JsonResponse('User is not authenticated', safe=False)
    else:
        customer = request.user.customer

        try:
            product = get_object_or_404(CardProduct, pk=productId)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        except ValueError:
            return JsonResponse('Not product', safe=False)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
        orderItem.save()
        if orderItem.quantity <= 0:
            orderItem.delete()
        return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = int(data['userFormData']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            adress=str(data['shippingInfo']['address']),
            city=data['shippingInfo']['city'],
            zip=data['shippingInfo']['zip'],
            phone=data['userFormData']['phone']

        )
    else:
        print('User is not logged in...')

    return JsonResponse('Payment complited', safe=False)