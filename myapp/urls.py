from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('aboutus',views.about,name='aboutus'),
    path('logindata',views.checklogin,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('contactus',views.contactus,name='contactus'),
    path('products/<int:catid>',views.allproduct,name='products'),
    path('productdetail/<int:proid>',views.productsingle,name='productdetails'),
    path('category',views.category,name='category'),
    path('addmessage',views.addmessage,name='addmessage'),
    path('inquiry/<int:id>',views.inquirypage,name='inquiry'),
    path('sendinquiry',views.sendinquiry,name='sendinquiry'),
    ]