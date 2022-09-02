from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def profile(request, pk):
    profile = get_object_or_404(Profile, pk=1)
    post = Post.objects.filter(author = pk)

    posts = Post.objects.filter(author = pk).count()
    context = {
        'posts' : post,
        'post' : posts,
        'profile' : profile,
    }
    return render(request, 'profile.html', context=context)
    
def register(request):
    return render(request, 'registr.html')
