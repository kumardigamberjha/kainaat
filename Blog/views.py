from django.shortcuts import render, redirect
from Blog.models import Blog
from Blog.forms import BlogForm
from django.contrib.auth.decorators import login_required

def BlogHome(request):
    blog = Blog.objects.all()
    randomeBlog = blog.order_by('?')[0]
    print(blog)
    context = {'Blog': blog, 'randomBlog': randomeBlog}
    return render(request, 'Blog/bloghome.html', context)


@login_required
def AddBlog(request):
    form = BlogForm()
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        title = request.POST['title']
        if Blog.objects.filter(title=title).exists():
            raise Exception("Blog Title Already Exists")

        if form.is_valid():
            form.save()
            return redirect("bloghome")
        else:
            print("Error: ", form.errors)
    
    context = {'form':form}
    return render(request, 'Blog/AddBlog.html', context)


def ReadBlog(request, post_id):
    data = Blog.objects.get(post_id=post_id)
    context = {'data': data}
    return render(request, 'Blog/read_blog.html', context)