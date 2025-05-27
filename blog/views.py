from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
class BlogListView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='my_post'

class BlogDetailView(DetailView):
    model = Post
    template_name='post_detail.html'
    context_object_name="detail"

class BlogCreateView(CreateView):
    model = Post
    template_name= 'post_new.html'
    fields ='__all__'

class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']
    
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    
    # reverse_lazy is used when you need to generate a URL at import time
    # or in a class attribute, while reverse() is used for generating URLs
    # during view execution. reverse_lazy is safer for class-based views
    # as it delays URL resolution until the view is actually called.