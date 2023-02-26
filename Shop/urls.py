from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.AllProds, name="all_prods"),

]