from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import A_Customer, Cart , Item
from supplier.models import Product
import re


# Create your views here.

# try:
#     customer_id
# except:
#     customer_id = -1

def signup(request):
    return render(request , "customer/signup.html")

def create_account(request):
    # return render(request , "/customer/home_page.html")
    if request.method == "POST":
        customer_name = request.POST.get("name","")
        contact = request.POST.get("contact","")
        password = request.POST.get("password","")
        confirm_password = request.POST.get("confirm_password","")
        encrypted = make_password(password)
        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        pattern_contact = "^\\+?[1-9][0-9]{7,14}$"

        print("inside if1")

        # try:
        fetching_details = A_Customer.objects.filter(contact=contact)
        print(fetching_details)

        if len(fetching_details) > 0:
            return render(request, 'customer/signup.html' , {'error_text':'Account Already Exists! Please Log in!'})
        else:

            if password != confirm_password:
                return render(request, 'customer/signup.html' , {'error_text':'Password does not match'})
            
            elif not(re.findall(pattern,password)):
                return render(request, 'customer/signup.html' , {'error_text':'Password is not strong enough!'})
            
            elif not(re.findall(pattern_contact , contact)):
                return render(request, 'customer/signup.html' , {'error_text':'Invalid Contact'})

            customer = A_Customer(customer_name=customer_name, contact = contact , password = encrypted)

            customer.save()

            kart = Cart(customer=customer)
            print(customer , kart)

            kart.save()
            print("inside if2")
            return redirect('/customer/')

        
        # except Exception as e:
        #     print(e)
        #     return render(request, 'customer/signup.html' , {'error_text':'Error creating account, please try again in some time '})
        
        


def home_page(request):
    # print(customer_id)
    try:
        print(request.session.get("id"))
        customer = A_Customer.objects.get(customerid = request.session.get("id") )
        print(customer)
        cart = Cart.objects.get(customer = customer)
        print(cart)
    except:
        return redirect("/customer/")


    Ele = Product.objects.filter(category = "Ele")
    Clo = Product.objects.filter(category = "Clo")
    Foo = Product.objects.filter(category = "Foo")
    Unc = Product.objects.filter(category = "Unc")

    

    data = {
        "categories":[Ele , Clo , Foo , Unc]
    }

    if request.method == "POST":
        
        productid = request.POST.get("productid")
        product = Product.objects.get(id = productid)
        amount = request.POST.get("amount")
        cart_items = cart.items.all()

        if int(amount) < 0:
            return redirect("/customer/home_page")


        present = False

        for i in cart_items:
            if i.product == product:
                i.amount += int(amount)
                i.save()
                present = True
                break
            else:
                pass
        
        if present == False:
            item = Item(product = product , amount = amount)
            item.save()
            cart.items.add(item)


    return render(request , "customer/homepage.html",data)



def login(request):
    print("hello")
    if request.method == "POST":
        contact = request.POST.get("contact","")
        password = request.POST.get("password","")

        try: 
            fetching_details = A_Customer.objects.filter(contact=contact).values("customerid",'contact','password' )
            print(fetching_details)
            hashed = fetching_details[0]['password']

            if len(fetching_details) > 0: # checking weather exists
                print("exists")
                if check_password(password,hashed): # checking password
                    print("correct pass")
                    # customer = A_customer.objects.get(contact=contact)
                    # customer_id = customer.customerid

                    

                    request.session["id"]= fetching_details[0]["customerid"]


                    return redirect('/customer/home_page') # correct

                else:
                    print("incorrect pass")
                    return render(request , 'customer/login.html' , {'error_text':'incorrect password'}) # incorrect

            else: # does not exist
                print("does not exist")
                return render(request , 'customer/login.html' , {'error_text':'account does not exist! Please Sign Up'})
        
        except Exception as e:
            print(e)
            return render(request , 'customer/login.html' , {'error_text':e} )
    else:
        return render(request,'customer/login.html')



def cart(request):
    print(dict(request.session))
    try:
        customer = A_Customer.objects.get(customerid = request.session.get("id") )
    except:
        return redirect("/customer/")
    cart = Cart.objects.get(customer = customer)

    cart_items = cart.items.all()


    data = {
        "cart":cart_items,
        "customer":customer,
        "total":cart.total()

    }

    

    if request.method == "POST":
        id = request.POST.get("itemid")
        item = Item.objects.get(id = id)
        amount = request.POST.get("amount")

        if int(amount) < 0:
            return redirect("/customer/home_page")
        
        if int(amount) == 0 :
            item.delete()
        else:
            item.amount = amount
            item.save()
    

        


    return render(request , "customer/cart.html",data)

def profile(request):

    try:
        customer = A_Customer.objects.get(customerid = request.session.get("id") )
        
    except:
        return redirect("/customer/")

    if request.method == "POST":
        name = request.POST.get("name")
        building = request.POST.get("building")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")

        customer.customer_name = name
        customer.building = building
        customer.street = street
        customer.city = city
        customer.state = state

        customer.save()

    data = {
        "customer":customer
    }

        



    return render(request , "customer/profile.html",data)

def search(request):


    if request.method == "GET":
        search = request.GET.get("search")

        if search:
            products = Product.objects.filter(name__contains=search)
    

            data ={
                "products":products
            }
        else:
            data = {}

    return render(request , "customer/search.html",data)

def checkout(request):
    
    

    customer = A_Customer.objects.get(customerid = request.session.get("id") )
    cart = Cart.objects.get(customer=customer)
    data = {
        "customer":customer,
        "cart":cart
    }

    print(customer,cart)

    if request.method == "POST":


        for item in cart.items.all():
            if item.amount > item.product.amount:
                error = item.product.name + ' has been deleted since there were only ' +  str(item.product.amount) + " in stock"
                data['error']=error
                item.delete()
                return render(request, "customer/checkout.html",data)
        for item in cart.items.all():
            item.product.amount -= item.amount
        cart.items.all().delete()


    
        

    return render(request , "customer/checkout.html",data)

