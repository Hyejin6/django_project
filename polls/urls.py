from django.urls import path
from . import views


# url 패턴(루트), 뷰, 이름
app_name = 'polls' # 네임스페이스 설정

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                               # ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),           # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  #ex: /polls/5/results.
    path('<int:question_id>/vote/', views.vote, name='vote'),          #ex: /polls/5/vote/
    # vote는 제너릭뷰 사용하지 않았으므로 그대로 놔두기
    path('<int:question_id>/chart/', views.result_chart, name='chart'),

]