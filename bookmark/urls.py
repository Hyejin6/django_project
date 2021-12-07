from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark' # 북마크 앱의 url에 namespace 설정하도록 변경

urlpatterns = [
    path('', BookmarkListView.as_view(), name = 'list'),
    path('add/', BookmarkCreateView.as_view(), name = 'add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
