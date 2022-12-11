from django.shortcuts import render
from Blog.models import Blog
from Blog.forms import BlogForm

def BlogHome(request):
    blog = Blog.objects.all()
    print(blog)
    context = {'Blog': blog}
    return render(request, 'Blog/bloghome.html', context)


def AddBlog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)

    context = {'form': form}
    return render(request, 'Blog/AddBlog.html', context)