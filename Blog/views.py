from django.shortcuts import render, redirect
from Blog.models import Blog, Comment
from Blog.forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required

def BlogHome(request):
    blog = Blog.objects.all()
    randomeBlog = blog.order_by('?')[0]
    randomeBlog2 = blog.order_by('?')[0]
    if randomeBlog == randomeBlog2:
        randomeBlog2 = blog.order_by('?')[0]

    print(blog)
    context = {'Blog': blog, 'randomBlog': randomeBlog,  'randomBlog2': randomeBlog2}
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


################## UPDATE #####################
@login_required
def UpdateBlog(request, post_id):
    data = Blog.objects.get(post_id = post_id)
    form = BlogForm(instance=data)
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=data)

        title = request.POST['title']
        if Blog.objects.filter(title=title).exists():
            raise Exception("Blog Title Already Exists")

        if form.is_valid():
            form.save()
            return redirect("bloghome")
        else:
            print("Error: ", form.errors)
    
    context = {'form':form}
    return render(request, 'Blog/update_blog.html', context)




def ReadBlog(request, post_id):
    data = Blog.objects.get(post_id=post_id)
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("bloghome")
        else:
            print("Error: ", form.errors)
    context = {'data': data, 'comment_form':form}
    return render(request, 'Blog/read_blog.html', context)