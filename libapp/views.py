from django.shortcuts import render,redirect
from .forms import ContactForm,userform,searchform
from .models import studentdata,bookdata
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from pymongo import MongoClient

    
def search(request):
    if request.method == 'POST':
            
            form = searchform(request.POST)
            if form.is_valid():
                                  
                book = request.POST['Book_name']
                bookname = bookdata.objects.filter(Book_name__contains=book) #to find book from database
                return render(request,'drop.html',{'bookname':bookname})
            else:
                form = searchform()          
                return render(request,'search.html',{'form':form})

    else:     
           form = searchform()          
           return render(request,'search.html',{'form':form})


def contact(request):
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form=form.save()
            return render(request,'form.html',{'form':form})
        return render(request,'form.html',{'form':form})
    return render(request,'form.html',{'form':form})


def login(request):
    form = userform()
    if request.method == 'POST':
        form= userform(request.POST)
        if form.is_valid():
            username = request.POST.get('Username')
            password = request.POST.get('password')

            log = studentdata.objects.filter(Username=username,password=password)
            if not log:
                # return HttpResponse('try again')
                return render(request,'login.html')
            else:
                return redirect('/search')
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})


