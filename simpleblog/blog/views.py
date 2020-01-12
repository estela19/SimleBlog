from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts=Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    context={
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)