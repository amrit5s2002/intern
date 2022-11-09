from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    p = Product.objects.all()
    pname=None
    pprice=None
    pquantity=None
    print("none  1")
    if request.method == 'GET':
        pname = request.GET.get('q')
        pprice = request.GET.get('price')
        pquantity = request.GET.get('quantity')
        new_obj = Product.objects.create(Product_Name = pname,
                          Price = pprice,
                          Quantity = pquantity)
    print("none  2")
    print(new_obj)
    return render(request,'home.html',{'p':p})