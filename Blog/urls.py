from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.BlogHome, name="bloghome"),
    path('addBlog/', views.AddBlog, name="AddBlog"),

]