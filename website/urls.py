from django.urls import path
from website import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('AboutUs/', views.AboutUs, name="aboutuspage"),
    path('ContactUs/', views.ContactUs, name="contactuspage"),

]