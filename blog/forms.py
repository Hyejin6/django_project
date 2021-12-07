from django import forms
from .models import Post

# PostForm이라는 클래스를 정의 -  장고의 forms의 ModelForm을 상속받음
class PostForm(forms.ModelForm): # 장고에서 제공하는 폼 형태

    class Meta: # 이 폼을 만들기위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문
        model = Post
        fields = ('title', 'text',) # 폼에 보여질 양식
        # 즉 글의 제목과 내용을 입력받겠다는 말임. 그 외 author은 현재 로그인하고 있는 사람, created_date는 글이 등록된 날짜도 있음
