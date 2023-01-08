from django.shortcuts import render
from website.forms import ContactUsForm
from django.contrib import messages
from Blog.models import Blog

def index(request):
    
    return render(request, 'website/welcomepage.html')

def HomePage(request):
    blogs = Blog.objects.all()[:6]
    context = {'blogs': blogs}
    return render(request, 'website/index.html', context)

def AboutUs(request):
    return render(request, 'website/aboutus.html')

def ContactUs(request):
    form = ContactUsForm()

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Feedback Form Submitted')
    context = {'form': form}
    return render(request, 'website/contactus.html', context)