import datetime
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import BlogArticle
from .forms import BlogArticleForm

# Create your views here.
def myview(request):
    #posts = BlogArticle.objects.all()
    posts = BlogArticle.objects.filter(is_published=True)
    return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogArticle, pk=pk)
    return render(request, 'post.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = BlogArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = datetime.datetime.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = BlogArticleForm()

    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(BlogArticle, pk=pk)
    if request.method == "POST":
        form = BlogArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = datetime.datetime.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = BlogArticleForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})