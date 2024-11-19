import os.path

from django.contrib.messages.context_processors import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from customers.forms import CustomerForm, OrderForm
from customers.models import Customer
import os
from django.contrib import messages
from django.shortcuts import get_object_or_404

from customers.serializers import CustomerSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    data = Customer.objects.all()
    context = {'data': data}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES)
        form2=OrderForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('contact')
    else:
        form=CustomerForm()
        form2=OrderForm()
    return render(request, 'contact.html', {'form':form,'form2':form2})



def update(request,id):
    customer =get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request,f'Customer updated successfully!{file_name} uploaded')
            else:
                messages.error(request,'Customer details updated successfully!')
                return redirect('about')
        else:
            messages.error(request,'Please confirm your changes')
    else:
        form=CustomerForm(instance=customer)
    return render(request, 'update.html', {'form':form,'customer':customer})

def delete(request,id):
    customer =get_object_or_404(Customer, id=id)

    try:
        customer.delete()
        messages.success(request,'Customer deleted successfully')
    except Exception as e:
        messages.error(request,'Customer not deleted')
    return redirect('about')

@api_view(['GET','POST'])
def Customersapi(request):
    if request.method == 'GET':
        customers =Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


