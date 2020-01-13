from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

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

def post_add(request):
    if request.method == 'POST':
        User = get_user_model()
        author = User.objects.get(username='admin')
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            author = author,
            title = title,
            content = content,
        )
        post.publish()
        post_pk = post.pk
        return redirect(post_detail, pk=post_pk) 

    elif request.method == "GET":
        return render(request, 'blog/post_add.html')