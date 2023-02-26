from django.forms import ModelForm

from Blog.models import Blog, Comment

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"