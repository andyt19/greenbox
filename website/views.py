from django.shortcuts import render, redirect
from website.models import Product, Warehouse
from website.forms import ProductForm, WarehouseForm
from django.http import HttpResponseNotFound

def addwarehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewall')
    else:
        form = WarehouseForm()
    context = {'form': form}
    return render(request, 'addwarehouse.html', context)

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewall')

    form = ProductForm()
    warehouses = Warehouse.objects.all()
    context = {'form': form, 'warehouses': warehouses}    
    return render(request, 'addproduct.html', context)

def viewall(request):
    products = Product.objects.all()
    warehouses = Warehouse.objects.all()
    context = {'products': products, 'warehouses': warehouses}
    return render(request, 'viewall.html', context)

def update(request, table, id):
    if table == 'product':
        # there probably is a better way to call the class via string but i'm not too sure
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST, instance=product)
    elif table == 'warehouse':
        warehouse = Warehouse.objects.get(id=id)
        form = WarehouseForm(request.POST, instance=warehouse)
    else:
        return HttpResponseNotFound(f'<h1>Table {table} not found</h1>')

    if form.is_valid():
        form.save()
        return redirect('/viewall')

def edit(request, table, id):
    if table == 'product':
        product = Product.objects.get(id=id)
        warehouses = Warehouse.objects.all()
        context = {'product': product, 'warehouses': warehouses}
        return render(request, 'editproduct.html', context)
    elif table == 'warehouse':
        warehouse = Warehouse.objects.get(id=id)
        context = {'warehouse': warehouse}
        return render(request, 'editwarehouse.html', context)
    else:
        return HttpResponseNotFound(f'<h1>Table {table} not found</h1>')
    
def delete(request, table, id):
    if table == 'product':
        item = Product.objects.get(id=id)
    elif table == 'warehouse':
        item = Warehouse.objects.get(id=id)     
    else:
        return HttpResponseNotFound(f'<h1>Table {table} not found</h1>')

    item.delete()
    return redirect('/viewall')