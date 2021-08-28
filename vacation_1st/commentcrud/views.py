from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from postcrud.models import Post

def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html', {'form':form, 'post':post})

def commentupdate(request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.method=='POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                    comment = form.save(commit=False)
                    comment.save()
                    return redirect('postshow', post_id=comment.post.pk)
            else:
                    return redirect('list')
        else:
            form = CommentForm(instance=comment)
            return render(request, 'postshow.html', {'form_comment': form, 'post': comment.post})

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('postshow', post_id=comment.post.pk)