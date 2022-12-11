from pyexpat import model
from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
# from taggit.managers import TaggableManager
# from taggit.models import TaggedItemBase



# Blogs Tags
# class BlogsTags(TaggedItemBase):
#     item = models.ForeignKey('AddBlog', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.item


# Playlist or Category
class Playlist(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Blog
class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField()
    pub_date = models.DateField(auto_now=True)
    # category = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    content = RichTextField()
    author= models.CharField(max_length=150, default="Tanya Gulati")
    readtime = models.IntegerField()

    def __str__(self):  
        return self.title