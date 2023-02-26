from django.forms import ModelForm
from Shop.models import Products, Cart, Booking

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"