from django.urls import path
from . import views

app_name = 'blog' # 블로그 앱의 url에 namespace 설정하도록 변경

urlpatterns = [ # url과 뷰 연결
    path('', views.post_list, name='post_list'),
    # '' : 끝에 blog가 오는 url요청이 오면 post_list뷰로 연결시켜주기
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # path 함수로 post_detail을 연결시켜주기 이 때 url은 post/<int:pk>/로 숫자형태의 값(pk)이 들어옴
    # 이 값이 들어왔을 때 post_detail로 연결해주고 패턴이름을 post_detail로 하기
    path('post/new/', views.post_new, name='post_new'),
    # post/new/ 형태의 url이 왔을 때, post_new라는 뷰함수로 연결 패턴이름은 post_new 정의
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 숫자 형태 + edit라는 url이 왔을 때, post_edit 뷰 함수로 연결 패턴이름은 post_edit 정의
]
