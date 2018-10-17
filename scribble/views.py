from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.

###########  POST  ###############################
#post all
def post_list(request):
    post = post.objects.all()
    return render(request, 'tunr/artist_list.html', {'posts': posts})

#get all
def post_detail(request, pk):
    post = post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

#post all
def artist_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', {'form': form})

#edit all
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'scribble/post_form.html', {'form': form})

#delete all
def post_delete(request, pk):
    post.objects.get(id=pk).delete()
    return redirect('post_list')

#############  Comment  ###############################
#post comment
def comment_list(request):
    comment = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comment': comments})

#get comment
def comment_detail(request, id):
  comment = comment.objects.get(id=id)
  return render(request, 'tunr/song_detail.html', {'song': song})

#get create
def comment_create(request):
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save()
      return redirect('comment_detail', id=comment.id)
  else:
    form = CommentForm()
  return render(request, 'scribble/comment_form.html', {'form': form})

#get edit
def comment_edit(request, id):
  comment = comment.objects.get(id=id)
  if request.method == 'POST':
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', id=comment.id)
  else:
    form = CommentForm(instance=comment)
  return render(request, 'scribble/comment_form.html', {'form': form})

#get delete
def comment_delete(request, id):
  Comment.objects.get(id=id).delete()
  return redirect('comment_list')
