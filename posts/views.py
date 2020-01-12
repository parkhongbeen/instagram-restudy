from django.shortcuts import render, redirect
from posts.forms import PostCreateForm
from posts.models import Post


def post_created(request):
    if request.method == 'POST':
        content = request.POST['content']
        images = request.FILES.getlist('images')
        post = Post.objects.create(author=request.user, content=content)
        for image in images:
            post.postimage_set.create(image=image)
        return redirect('posts:post_list')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }
    return render(request, 'posts/postcreate.html', context)


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/postlist.html', context)
