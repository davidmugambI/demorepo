from django.shortcuts import render, redirect, get_object_or_404
from inventoryapp.forms import DesktopForm, LaptopForm, MobileForm
from django.contrib import messages
from inventoryapp.models import Desktop,Laptop,Mobile

# Create your views here.
def index(request):
    return render(request, 'inventoryapp/index.html')

def desktopCreateView(request):
    if request.method == 'POST':
        form = DesktopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Desktop item added')
            return redirect('index')

    else:
        form = DesktopForm()
    context = {'form': form,'color':'blue','header':'Add Desktop'}
    return render(request, 'inventoryapp/create.html',context)

def laptopCreateView(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Laptop item added')
            return redirect('index')

    else:
        form = LaptopForm()
    context = {'form': form,'color':'green','header':'Add Laptop'}
    return render(request, 'inventoryapp/create.html',context)
def mobileCreateView(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mobile item added')
            return redirect('index')

    else:
        form = MobileForm()
    context = {'form': form,'color':'black','header':'Add Mobile'}
    return render(request, 'inventoryapp/create.html',context)

def retrieveDesktopView(request):
    items = Desktop.objects.all()
    context = {'items':items, 'header': 'Desktop'}
    return render(request, 'inventoryapp/index.html', context)

def retrieveLaptopView(request):
    items = Laptop.objects.all()
    context = {'items':items,'header': 'Laptop'}
    return render(request, 'inventoryapp/index.html', context)

def retrieveMobileView(request):
    items = Mobile.objects.all()
    context = {'items':items,'header': 'Mobile'}
    return render(request, 'inventoryapp/index.html', context)

def edit_desktop(request, pk):
    item = get_object_or_404(Desktop, pk=pk)
    if request.method == 'POST':
        form = DesktopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully Updated")
            return redirect('index')
    else:
        form = DesktopForm(instance=item)

    return render(request, 'inventoryapp/edit_item.html',{'form':form})

def edit_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully Updated")
            return redirect('index')
    else:
        form = LaptopForm(instance=item)

    return render(request, 'inventoryapp/edit_item.html',{'form':form})

def edit_mobile(request, pk):
    item = get_object_or_404(Mobile, pk=pk)
    if request.method == 'POST':
        form = MobileForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully Updated")
            return redirect('index')
    else:
        form = MobileForm(instance=item)

    return render(request, 'inventoryapp/edit_item.html',{'form':form})

def delete_device(request, pk, model):
    model.objects.filter(id=pk).delete()
    items = model.objects.all()
    context = {'items': items}
    return render(request, 'inventoryapp/index.html', context)

def delete_desktop(request,pk):
    return delete_device(request,pk,Desktop)

def delete_laptop(request,pk):
    return delete_device(request,pk,Laptop)

def delete_mobile(request,pk):
    return delete_device(request,pk,Mobile)

