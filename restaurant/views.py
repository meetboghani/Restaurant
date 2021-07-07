from django.shortcuts import render,redirect
from .models import Gallery
from .models import Chef
from .models import testimonal, Party, SpecialItem
from restaurant.models import Contact,Reservations,Menus1
from django.contrib import messages


# Create your views here.
def index(request):

    gallerys = Gallery.objects.all()
    chefs = Chef.objects.all()
    testimonals = testimonal.objects.all()
    parties = Party.objects.all()
    special = SpecialItem.objects.all()
    menu = Menus1.objects.all()
    reserve = Reservations.objects.all() 

    return render(request,"index.html",{'gallerys': gallerys,'chefs': chefs, 'testimonals':testimonals,'parties': parties, 'special':special, 'menu':menu, 'reserve':reserve})

def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        cnt = Contact(name3=name, email=email, subject=subject, message=message)
        cnt.save();
        messages.success(request, 'Message sent successfully')
        return redirect('/')

    else:
        return(request,'index.html')

def reservation(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message1 = request.POST['message']

        rst = Reservations(name4=name, email1=email, phone=phone, date=date, time=time, people=people, message1=message1)
        rst.save();
        
        return redirect('/')

    else:
        return(request,'index.html')