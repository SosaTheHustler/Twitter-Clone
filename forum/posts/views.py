from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    form = PostForm(request.POST, request.FILES)
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

            # No, Show Error
        else:
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html',
                    {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
<<<<<<< HEAD

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
       form = PostForm(request.POST, request.FILES, instance=post)
        # If the form is valid
       if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

            # No, Show Error
       else:
            form = PostForm(PostForm)
            return HttpResponseRedirect(form.errors.as_json)
    return render(request, 'edit.html', {'post':post})
            
def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes +1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
=======
>>>>>>> bba7967e0142db0b2effb0b7ccb28e53f831396b
