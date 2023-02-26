from django.shortcuts import render
from Shop.models import Products, Cart, Booking
from Shop.forms import ProductForm, CartForm, BookingForm



def AllProds(request):
    form = CartForm()
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Error: ", form.errors)
    context = {'form': form}
    return render(request, 'Shop/allProds.html', )


def AddCartview(request):
    return render(request, 'Shop/allProds.html')


def ShowCart(request):
    return render(request, 'Shop/allProds.html')


def ViewCart(request):
    return render(request, 'Shop/allProds.html')