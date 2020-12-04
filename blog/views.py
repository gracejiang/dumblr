from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

from markdown2 import Markdown

# Create your views here.

# splash page
def splash_page(request):
    return render(request, 'blog/splash.html')

# blog posts page
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# post details
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post, 'html': markdown_to_html(post.text)})

def markdown_to_html(md):
    markdowner = Markdown()
    return markdowner.convert(md)
