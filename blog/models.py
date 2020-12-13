from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def  publish(self):
        """ブログを公開するメソッド
        
        クラス自体をブログの内容として公開するためのメソッド
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """ブログのタイトルを返す関数
        
        __str__メソッドを呼ぶと、ブログのタイトルをリターンする
        """
        return self.title