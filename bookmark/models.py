from django.db import models
from django.urls import reverse

# Create your models here.

# models.Model을 상속받는 Bookmark 클래스 생성
class Bookmark(models.Model) :
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self): # __str__메서드는 항상 문자열을 반환해야 함
        return "이름 : " + self.site_name + ", 주소 : " + self.url # 출력내용

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])

