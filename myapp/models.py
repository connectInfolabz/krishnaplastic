from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now=True)
    uimg=models.ImageField(upload_to="profile")

    def profile(self):
        return mark_safe('<img src="{}" width="100">'.format(self.uimg.url))


class Category(models.Model):
    catname=models.CharField(max_length=100,verbose_name='Category Name')
    catimage=models.ImageField(upload_to='categoryImg',verbose_name='Category Image')


    def __str__(self):
        return self.catname

    def  categorypic(self):
        return mark_safe('<img src="{}" width="100">'.format(self.catimage.url))

class Color(models.Model):
    color=models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Product(models.Model):
    catid=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category Id')
    name=models.CharField(max_length=100)
    shape=models.CharField(max_length=100)
    usage=models.CharField(max_length=100)
    size=models.CharField(max_length=50)
    material_type=models.CharField(max_length=50)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    price=models.FloatField()
    description=models.TextField()
    quantity=models.FloatField()
    image=models.ImageField(upload_to='productImg')
    status=models.CharField(max_length=50,
                            choices=[('available','Available'),
                                     ('not available','Not Available')])
    def photo(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))

    def __str__(self):
        return self.name
class ProductImages(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='extraImg')

    def photo(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))

class ProductInquiry(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.FloatField()
    budget=models.FloatField()
    message=models.TextField()
    inquirystatus=models.CharField(max_length=50,choices=
    [('pending','Pending'),('resolved','Resolved')],default='pending')
    timestamp=models.DateTimeField(auto_now=True)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50, choices=
    [('pending','Pending'),('resolved','Resolved')],default='pending')