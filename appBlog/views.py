from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})


def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    comments=post.comments.all()

    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            return redirect('post_detail',id=post.id)
    else:
        comment_form=CommentForm()

    context={
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'post_edit.html',context)



def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('post_detail',id=post.id)
    else:
        form=PostForm()
    
    context={
        'form':form,
    }
    return render(request,'post_edit.html',context)


def post_edit(request,id):
    post=get_object_or_404(Post, id=id)

    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(request, 'post_detail', id=post.id)
    else:
        form=PostForm(instance=post)
    
    context={
        'form':form,
        'post':post,
    }
    return render(request,'post_edit.html',context)
    

def post_delete(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('index')