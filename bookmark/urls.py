from django.urls import path
from .views import BookmarkListVew, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark' # name space 설정

urlpatterns = [
    #클래스형 뷰이기때문에 as_view() 사용 (함수형 뷰는 뷰 이름만 써주면 됨)
    path('', BookmarkListVew.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]