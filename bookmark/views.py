from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from . models import Bookmark
from django.urls import reverse_lazy

# Create your views here.

class BookmarkListVew(ListView) :
    model = Bookmark
    paginate_by = 6 # 페이지당 6건 지정 (페이징 기능)
    # 현재 뜨는 오류 -> UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'bookmark.models.Bookmark'> QuerySet.
    # 해결방법 : 정렬 순서를 지정해주어야 함.
    # 단 실질적인 큰 오류가 아닌 경고일뿐이므로 꼭 추가해줄 필요는 없음.
    # ordering = ['id']

class BookmarkCreateView(CreateView) :
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView) :
    model = Bookmark

class BookmarkUpdateView(UpdateView) :
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('bookmark:list') # success_url 은 목록 페이지로 가도록 reverse_lazy를 사용해 설정

