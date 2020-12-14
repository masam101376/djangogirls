from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    """Postの一覧を表示する関数
    
    models.pyに定義した、ポストの内容を保存するためのモデルPostにあるものを表示する
    """
    return render(request, 'blog/post_list.html', {})
