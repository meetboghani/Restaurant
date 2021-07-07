from django.db import models
from datetime import date, datetime


# Create your models here.

class Gallery(models.Model):

    img = models.ImageField(upload_to = 'pics')

class Chef(models.Model):

    img1 = models.ImageField(upload_to = 'chef')
    name = models.CharField(max_length=100)

class testimonal(models.Model):

    img2 = models.ImageField(upload_to = 'testimonal')
    decription = models.TextField()
    name1 = models.CharField(max_length=100) 

class Party(models.Model):

    img3 = models.ImageField(upload_to = 'parties')
    price = models.IntegerField()
    party = models.CharField(max_length=80)
    content = models.TextField()
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    allocate = models.CharField(max_length=50)

class SpecialItem(models.Model):

    img4 = models.ImageField(upload_to = 'specialitems')
    dishname = models.CharField(max_length = 50)
    name2 = models.CharField(max_length = 50)
    desc = models.TextField()
    num = models.IntegerField()

class Contact(models.Model):

    name3 = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

class Reservations(models.Model):

    name4 = models.CharField(max_length=50)
    email1 = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message1 = models.TextField()

class Menus1(models.Model):

    dish = models.CharField(max_length=50)
    ingredients = models.TextField()
    img5 = models.ImageField(upload_to = 'menu')
    price1 = models.IntegerField()
    Type = models.CharField(max_length=50) 

