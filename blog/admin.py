from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) # Post라는 사이트를 우리가 접근할 수 있도록 어드민에 등록
