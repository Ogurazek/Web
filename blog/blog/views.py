from django.shortcuts import render
from apps.posts.models import Post

def index(request):
    post_recientes = Post.objects.order_by('-fecha') [:3]
    return render(request, 'index.html', {'post_recientes': post_recientes})





