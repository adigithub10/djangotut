from django.shortcuts import render
from.models import Post
from django.http import HttpResponse
from django.http import HttpRequest

def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request ,'posts/posts_list.html',{'posts':posts})



def post_page(request , slug) :
     return HttpResponse(slug)