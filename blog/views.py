from django.shortcuts import render

from blog.models import BlogArticle

# Create your views here.
def myview(request):
    #posts = BlogArticle.objects.all()
    posts = BlogArticle.objects.filter(is_published=True)
    return render(request, 'default.html', {'posts':posts})
