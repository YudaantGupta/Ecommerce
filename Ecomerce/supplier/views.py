from django.shortcuts import render,redirect
from .models import Product
from .forms import Form

# Create your views here.

def idthing(request,id):
     product = Product.objects.get(id=id)

     data = {"product" : product}

     return render(request, "supplier/idthing.html", data)


def product(request):
    x = Product.objects.all()
    y = {"product":x , "lenght":len(x)}
    return render(request , "supplier/product.html" , y)


def add(request):
    product_form = Form()

    if request.method == "POST":
        # name = request.POST.get("name","")
        # price = request.POST.get("price","")
        # amnt = request.POST.get("amnt","")
        # disc=request.POST.get("disc","")
        # description= request.POST.get("description","")
        # inStock=request.POST.get("inStock","")

        # if inStock == "on":
        #     inStock = True
        # else:
        #     inStock = False

        # print(request.POST)

        # product = Product(name = name, price = price , amount = amnt , disc = disc , description=description,inStock=inStock)

        product_form = Form(request.POST,request.FILES)
        if(product_form.is_valid()):
            product_form.save()

        

        
        return redirect("/supplier/product")

        
    data={"product_form":Form()}
    return render(request , "supplier/add_orders.html",data)
