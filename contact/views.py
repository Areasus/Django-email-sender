from multiprocessing import context
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    context={
        "title":"Home page"
    }
    return render(request,"index.html",context)

def contact(request):
    context={
        "title":"Contact Us"
    }
    if request.method== 'POST':
        print(request.POST)
        name = request.POST.get('studentName')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('remarks')
        smessage = '''
            <h1>From</h1> {}
                Helo, {}
        '''.format(email,message)
        data ={
            "name":name,
            "subject":"Query from website",
            "mobile":mobile,
            "message":message,
        }
        send_mail(data["subject"],smessage,email,['emosion.punk@gmail.com'])
    return render(request,"contact.html",context)