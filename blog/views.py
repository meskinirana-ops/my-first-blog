from django.shortcuts import render
from .models import Post  # si tu as un modèle Post

def post_list(request):
    posts = Post.objects.all()  # récupère tous les posts
    return render(request, 'blog/post_list.html', {'posts': posts})
