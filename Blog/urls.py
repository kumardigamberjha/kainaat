from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.BlogHome, name="bloghome"),
    path('addBlog/', views.AddBlog, name="AddBlog"),
    path('updateBlog/<int:post_id>/', views.UpdateBlog, name="updateBlog"),

    path('readBlog/<str:title>/', views.ReadBlog, name="ReadBlog"),
]