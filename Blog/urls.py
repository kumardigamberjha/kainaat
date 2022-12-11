from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.BlogHome, name="bloghome"),
    path('addBlog/', views.AddBlog, name="AddBlog"),
    path('readBlog/<int:post_id>/', views.ReadBlog, name="ReadBlog"),
]