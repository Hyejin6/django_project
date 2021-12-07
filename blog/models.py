from django.db import models
from django.conf import settings
from django.utils import timezone ## 시간을 사용하기 위해 import 선언

# Create your models here.

class Post(models.Model):   # models.Model을 상속받아서 클래스 형태로 정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # author = 저자, 즉 작성한 사람을 의미. 그 사람을 외래키로 설정
    title = models.CharField(max_length=200) # 게시글의 제목 (최대 200까지 가능)
    text = models.TextField() # 게시글의 글 부분
    created_date = models.DateTimeField(default=timezone.now)  # created_date : 블로그가 처음 생성된 시기
    # ↑ DateTimeField 정의 - 기본값으로 timezone.now(현재시간) 설정 즉, 데이터가 추가되는 시간을 받아온다. 어떤 게시글이 처음 생성된 시간
    published_date = models.DateTimeField(blank=True, null=True) # DateTimeField 정의 - blank=True, null=True 설정

    def publish(self):
        self.published_date = timezone.now() # 이 게시글이 게시된 시기
        self.save() # 저장

    def __str__(self):
        return self.title # 타이틀 리턴