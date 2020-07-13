from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def postshow(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postshow.html', {'post': post})

def postnew(request):
    return render(request, 'postnew.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
        else:
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'postnew.html', {'form': form})