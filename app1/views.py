from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

def all_comp(request):
    pr = product.objects.all()
    cm = costumer.objects.all()
    orde = orders.objects.all()

    context = {
        'title': 'CompanyTitle',
        'product': pr,
        'customer': cm,
        'order': orde
    }
    return render(request, 'index.html', context=context)


def cust_read(request,pk):
    orde = orders.objects.filter(costumer_id=pk)
    cm = costumer.objects.get(pk=pk)

    context = {
        'title': 'CompanyTitle',
        'customer': cm,
        'order': orde
    }
    return render(request, 'customer_read.html', context=context)


def or_read(request,pk):
    cm = costumer.objects.all()
    pr = product.objects.all()
    orde = orders.objects.filter(pk=pk)

    context = {
        'title': 'CompanyTitle',
        'customer': cm,
        'product': pr,
        'order': orde
    }
    return render(request, 'order_read.html', context=context)


def pr_read(request, pk):
    product_obj = get_object_or_404(product, pk=pk)
    product_list = product.objects.all()
    order_list = orders.objects.filter(product_id=product_obj)

    context = {
        'product': product_obj,
        'product_list': product_list,
        'order': order_list
    }
    return render(request, 'product_read.html', context=context)


def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pr = product.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {"form": form})

def add_orders(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pr = orders.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = OrderForm()

    return render(request, 'add_order.html', {"form": form})

def add_customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            pr = costumer.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = CustomerForm()

    return render(request, 'add_customer.html', {"form": form})


