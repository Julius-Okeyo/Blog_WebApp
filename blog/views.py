from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template = "home.html"
