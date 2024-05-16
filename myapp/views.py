from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from . models import *


def indexpage(request):
    return render(request,'home-two.html')


def about(request):
    return render(request,'about-us.html')


def contactus(request):
    return render(request,'contact-us.html')


def productsingle(request,proid):
    catdata = Category.objects.all()
    singledata = Product.objects.get(id=proid)
    productimages = ProductImages.objects.get(productid=singledata)
    context = {
        'singledata': singledata,
        'catdata': catdata,
        'prodimage':productimages
    }
    return render(request,'productsingle.html',context)


def allproduct(request,catid):
    products = Product.objects.filter(catid=Category(id=catid)).exclude(status='not available')
    context = {
        'products': products
    }
    return render(request,'allproducts.html',context)


def category(request):
    catdata = Category.objects.all()
    context = {
        'catdata': catdata
    }
    return render(request,'productcat.html',context)


def addmessage(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            data = Contact(name=name,email=email,phone=phone,message=message)
            data.save()
            messages.success(request,'Thanks for you message')
            return redirect(contactus)
    except:
        return redirect(indexpage)


def checklogin(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("pass")
            user = User.objects.get(email=email, password=password)
            try:
                request.session['log_email'] = user.email
                request.session['log_id'] = user.id
                request.session.save()
            except User.DoesNotExist:
                user = None
            if user is not None:
                messages.success(request,"Successfullt Log In !")
                return redirect(indexpage)
    except:
        messages.error(request,"Please enter correct email and password")
        return redirect(indexpage)


def register(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            pwd = request.POST.get("pass")
            photo = request.FILES["photo"]

            data = User(name=name, email=email, phone=phone, password=pwd,uimg=photo)
            data.save()
            messages.success(request, "Data Inserted Successfully. You can Login now")
            return redirect(indexpage)
        else:
            messages.error(request, "Error occured")
            return redirect(indexpage)
    except Exception as e:
        print("vsnvjnd\n",e)
        return redirect(indexpage)


def logout(request):
    try:
        if request.session['log_id'] is not None:
            del request.session['log_email']
            del request.session['log_id']
            return redirect(indexpage)
    except:
        return redirect(indexpage)


def inquirypage(request,id):
    try:
        if request.session['log_id'] is not None:
            uid = request.session['log_id']
            data = User.objects.get(id=uid)
            productdata = Product.objects.get(id=id)
            context = {
                'id':id,
                'userid':uid,
                'data':data,
                'productdata':productdata
            }
            return render(request,'inquiry.html',context)
    except Exception as e:
        print("Error",e)
        return redirect(indexpage)


def sendinquiry(request):
    try:
        if request.session['log_id'] is not None:
            uid = request.session['log_id']
            if request.method == "POST":
                    proid = request.POST.get("proid")
                    quantity = request.POST.get("quantity")
                    budget = request.POST.get("budget")
                    message = request.POST.get("message")

                    data = ProductInquiry(productid=Product(id=proid),userid=User(id=uid),quantity=quantity, budget=budget, message=message)
                    data.save()
                    messages.success(request, "Your inquiry has submitted.")
                    return redirect(indexpage)
            else:
                    messages.error(request, "Error occured")
                    return redirect(indexpage)
    except Exception as e:
        print("Error",e)
        return redirect(indexpage)