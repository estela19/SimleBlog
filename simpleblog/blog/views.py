from django.shortcuts import render, get_object_or_404
from blog.models import Post

def post_list(request):
    posts=Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    context={
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context={
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)
