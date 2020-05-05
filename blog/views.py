from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .form import BlogPostModelForm


def getAllBlogs(request):
    # blogs = BlogPost.objects.published() #filter(title__icontains='pos') #all()
    blogs = BlogPost.objects.all() #filter(title__icontains='pos') #all()
    blogs = blogs.filter(user=request.user)
    return render(request, 'blog/all.html', {"blogs": blogs})


def getBlogDetail(request, slug):
    # blog = BlogPost.objects.filter(slug=slug)
    # if blog.count() == 0:
        # raise Http404
    # blog = blog.first()
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/details.html', {"blog": blog})

# @login_required
def createBlog(request):
    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        # obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        # print(obj)
        obj.save()
        form = BlogPostModelForm()
    
    return render(request, 'blog/create.html', {'form': form})


def updateBlog(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        form = BlogPostModelForm()
        return redirect('/blog')
    return render(request, 'blog/update.html', {'form': form, 'title': f"Update {obj.title}"})


def destroyBlog(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    return render(request, 'blog/delete.html', {'title': obj.title})


# def getUsersBlogs(request):
#     from blog.models import BlogPost
#     from django.contrib.auth import get_user_model
#     User=get_user_model()
#     j=User.objects.first()
#     j.blogpost_set.all()

#     qs = BlogPost.objects.filter(user__id=j.id)
#     qs
