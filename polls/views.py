from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic # 제너릭
import json

# Create your views here.

# 클래스형뷰(제너릭뷰)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    """Return the last five published questions."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#      # return HttpResponse("2005905 김혜진 Hello, world. You're at the polls index.") # 뷰 생성 메시지 출력
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5] # 등록한 질문을 역순으로 정렬(최근등록이 위로) 그리고 최대 5개까지만 가져오라는 뜻
#     # output = ', '.join([q.question_text for q in latest_question_list]) # 콤마와 묶어서 리스트 보여주기
#     # return HttpResponse(output)
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 등록한 질문을 역순으로 정렬(최근등록이 위로) 그리고 최대 5개까지만 가져오라는 뜻
#     # template = loader.get_template('polls/index.html')
#     context = {'latest_question_list' : latest_question_list}
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context) # render 함수로 응답을 보내줌
#
# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." %question_id)
#     # try: question = Question.objects.get(pk = question_id)
#     # except Question.DoseNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question' : question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     # response = HttpResponse("You're looking at the results of question %s." %question_id)
#     # return response
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})  # 각 답변 항목과 투표 수를 한꺼번에 보여줌

# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." %question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])  # 라디오버튼으로 선택한 답변 id 찾아오기
#     except(KeyError, Choice.DoesNotExist):  # 예외발생 - 못찾은 경우
#         return render(request, 'polls/detail.html', {  # 에러메시지를 담아 render함수 전달
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1  # 선택한 답변의 카운트를 1 증가시킴
#         selected_choice.save()  # 변경된 사항 저장
#
#         # 지정된 url 페이지로 리다이렉트 할 때 사용
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))  # 여기 끝에 쉼표 넣어야 함


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." %question_id)
    question = get_object_or_404(Question, pk=question_id)
    # print("[DEBUG_CHOISE] ", request.POST['choice']) # 출력 확인용

    for id_check in request.POST.getlist('choice'): # 체크박스로 선택한 답변 가져오기
        try:
            selected_choice = question.choice_set.get(pk=id_check)  # 체크박스로 선택한 답변 id 찾아오기
        except(KeyError, Choice.DoesNotExist):  # 예외발생 - 못찾은 경우
            return render(request, 'polls/detail.html', {  # 에러메시지를 담아 render함수 전달
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1  # 선택한 답변의 카운트를 1 증가시킴
            selected_choice.save()  # 변경된 사항 저장

            # 지정된 url 페이지로 리다이렉트 할 때 사용
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))  # 여기 끝에 쉼표 넣어야 함



# 차트 만들기 기능
def make_chart_data(data_question) :

    my_data = list()
    for choice in data_question.choice_set.all() :
        my_dict = dict()
        my_dict['name'] = choice.choice_text
        my_dict['y'] = choice.votes
        my_data.append(my_dict)

    chart_data = [{
        'name' : 'Votes',
        'colorByPoint' : 'true',
        'data' : my_data,
    }]

    return chart_data


# 차트 결과화면 기능
def result_chart(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)

    chart_data = make_chart_data(question)
    dump = json.dumps(chart_data)

    chart_title = {
        'text': '투표결과 <br>' + question.question_text
    }

    dump_title = json.dumps(chart_title)

    return render(request, 'polls/chart.html', {'chart_data' : dump, 'chart_title' : dump_title})

