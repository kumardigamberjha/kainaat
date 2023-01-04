from django.shortcuts import render
from website.forms import ContactUsForm
from django.contrib import messages


def index(request):
    return render(request, 'website/welcomepage.html')

def HomePage(request):
    return render(request, 'website/index.html')

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