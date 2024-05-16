from django.contrib import admin
from .models import *
# Register your models here.


class Showuser(admin.ModelAdmin):
    list_display = ['name','email','phone','password','profile','timestamp']


admin.site.register(User,Showuser)


class Showmessages(admin.ModelAdmin):
    list_display = ['name','email','phone','message','status','timestamp']


admin.site.register(Contact,Showmessages)


class Showcategory(admin.ModelAdmin):
    list_display = ['catname','categorypic']


admin.site.register(Category,Showcategory)


class Showcolor(admin.ModelAdmin):
    list_display = ['color']


admin.site.register(Color,Showcolor)


class Showproduct(admin.ModelAdmin):
    list_display = ['catid','name','photo','shape','usage','size','material_type','color','price','description','quantity','status']


admin.site.register(Product,Showproduct)


class Showimages(admin.ModelAdmin):
    list_display = ['productid','photo']


admin.site.register(ProductImages,Showimages)


class Showinquiry(admin.ModelAdmin):
    list_display = ['productid','userid','quantity','budget','message','inquirystatus','timestamp']


admin.site.register(ProductInquiry,Showinquiry)