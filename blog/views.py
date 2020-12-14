from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    """Postの一覧を表示する関数
    
    models.pyに定義した、ポストの内容を保存するためのモデルPostにあるものを表示する
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
