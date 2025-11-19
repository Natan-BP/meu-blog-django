# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 404 se não existir
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # sem validação "chique" nessa versão — pode deixar bruto
        post = Post.objects.create(title=title, content=content)
        return redirect('post-detail', pk=post.pk)

    return render(request, 'blog/post_form.html', {'action': 'create'})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post-detail', pk=post.pk)

    context = {
        'action': 'update',
        'post': post,
    }
    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post-list')

    # GET → mostra página de confirmação
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
