from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
import datetime
# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method=='POST':
        username=request.POST.get['username']
        password=request.POST['password']
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect('home')
        else:
            messages.success(request,"Login failed!")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out....")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You have registered succesfully... , Welcome!")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def record(request,pk):
    if request.user.is_authenticated:
        record=Record.objects.get(id=pk)
        x=str(record.created_at)
        y=x[8:10]
        z=str(datetime.datetime.now())
        p=z[8:10]
        q=int(p)-int(y)
        if q==0:
            days_before="today"
        elif q==1:
            days_before="yesterday"
        else:
            days_before=f"{q} days ago"
        return render(request,'record.html',{'record':record ,'days_before':days_before})
    else:
        messages.success(request,"Please login to view the records!!")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted successfully...")
        return redirect('home')
    else:
        messages.success(request,"Please login to modify the records!!")
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        form=AddRecordForm(request.POST or None)
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record Added successfully..")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"Please login to add records!")
        return redirect('home')