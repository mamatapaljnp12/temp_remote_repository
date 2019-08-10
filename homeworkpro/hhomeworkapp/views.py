from django.shortcuts import render
from .forms import ContactForm
from .models import ContactData
from django.http.response import HttpResponse

def Contactview(request):
    if request.method =='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name','')
            contactnumber1=request.POST.get('contactnumber','')
            email1=request.POST.get('email','')
            address1=request.POST.get('address','')
            a=ContactData(name=name1,contactnumber=contactnumber1,email=email1,address=address1)
            a.save()
            msg="All Data Fill"
            cform=ContactForm()
            return render(request,'index.html',{'abcd':cform,'aaama':msg})


        else:
            return HttpResponse('invalid data')
    else:
        cform = ContactForm()
        return render(request, 'index.html', {'abcd': cform})

def FatchingData(request):
    data=ContactData.objects.all()
    return render(request,'home.html',{'data':data})




