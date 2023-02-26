from django.shortcuts import render
from website.forms import ContactUsForm
from django.contrib import messages
from Blog.models import Blog


def HomePage(request):
    blogs = Blog.objects.all()[:6]
    form = ContactUsForm()

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Feedback Form Submitted')
    context = {'blogs': blogs, 'form': form}
    return render(request, 'website/index.html', context)

def AboutUs(request):
    return render(request, 'website/about.html')

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