from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 


class BloggingListView(ListView):
    queryset = Post.objects.order_by('-published_date')
    template_name = 'blogging/list.html'


class BloggingDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
