from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse
# Create your views here.
from .forms import FormBlog

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return  render(request, 'page/index.html', context)

def formblog(request):
     form = FormBlog()
     if request.method == 'POST':
         form = FormBlog(request.POST)
         if form.is_valid():
             form.save()
             return redirect('index')

         else:
             form = FormBlog()
     context= {'form': form}
     return render(request, 'page/form.html', context)


def editblog(request, pk):
    post = Post.objects.get(id=pk)
    form = FormBlog(instance=post)

    if request.method == 'POST':
        form = FormBlog(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            form = FormBlog()
    context = {'form': form}


    return  render(request, 'page/editblog.html', context)


def deleteblog(request, pk):
    post = Post.objects.get(id=pk)
    if request.method =="POST":
         post.delete()
         return  redirect('index')
    return render(request, 'page/delete.html', context={'post': post})