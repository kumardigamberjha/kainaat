from django.shortcuts import render

def BlogHome(request):
    return render(request, 'Blog/bloghome.html')