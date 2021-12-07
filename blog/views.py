from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone # 시간을 사용하기 위해 import
from .models import Post # Post 사용하기 위해 정의
from .forms import PostForm

# Create your views here.

# ★함수형 뷰는 항상 request를 매개변수로 받음
def post_list(request): # 목록에 대한 뷰를 request를 받는 함수형으로 정의
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # ↑ Post에 저장되어 있는 여러개의 objects 중에서 필터를 통해서 해당되는 조건에 맞는 것만 골라내어
    # ↑ 포스팅 된 글들 목록중에서 published_date가 현재시간보다 작거나 같은 Post만 필터링해서 posts에 넣기
    # ↑ published_date : 정렬하기
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 장고의 뷰에서 일련의 처리가 끝난 후 리턴값으로 render

def post_detail(request, pk): # 함수형으로 정의 - 상세페이지이기 때문에 list에서 선택한 글을 DB에서 읽어다가 그 글에 대한 정보를 화면에 출력
    post = get_object_or_404(Post, pk=pk) # get_object_or_404를 이용해서 요청받은 글의 번호(PK값)로 해당되는 글을 찾는다.
    # 모델인 POST에서 PK가 요청받은 PK를 가지고 해당글을 찾아서 변수 post에 넣는다
    return render(request, 'blog/post_detail.html', {'post': post})
    # render함수가 하는 일 - 이렇게 가지고온 post를 갖고 blog/post_detail.html과 함께 reponse로 보냄.

def post_new(request): # 함수형으로 정의 - 블로그 글 추가
    if request.method == "POST": # request에서 가지고 있는 메서드가 POST이면
        # 사용자가 form에 제목이나 글을 입력을 하고 저장을 하면 request 메서드가 POST로 전달이 됨
        form = PostForm(request.POST)
        if form.is_valid(): # is_valid()함수를 통해서 form의 값들이 바른지 체크(바르면 아래내용 실행)
            post = form.save(commit=False) # 받아온 값들을 저장 - commit=False는 바로 저장하지 말라는 것
            post.author = request.user # 저자 = 글을 쓴 사람(유저)
            post.published_date = timezone.now() # 글을 쓴 시간 = 지금 시간
            post.save() # 저장버튼 - 실제로 이 때 db에 저장이 된다.
            return redirect('blog:post_detail', pk=post.pk) # redirect 메서드 호출해서 post_detail로 연결 - 즉 글쓰고 저장완료시 post_detail화면으로 이동하라는 뜻
    else: # request에서 가지고 있는 메서드가 POST가 아니면 (GET이면)
        form = PostForm() # form에 PostForm()을 할당 - 즉 비어있는 form을 보여주라는 뜻 (사용자에게 입력받을 수 있는 폼 형식을 보여줌)
    return render(request, 'blog/post_edit.html', {'form': form}) # render함수를 리턴, post_edit.html을 리턴 및 form 변수에 form을 할당

def post_edit(request, pk): # 함수형으로 정의 - 블로그 글 수정
    post = get_object_or_404(Post, pk=pk) # pk를 가지고 db에서 글의 내용을 가지고 와서 post에 넣음
    if request.method == "POST": # request에서 가지고 있는 메서드가 POST이면
        form = PostForm(request.POST, instance=post) # instance=post를 넣음 - 즉 비어잇는 폼에 post를 담음
        if form.is_valid(): # 받아온 form이 유효한지 확인
            post = form.save(commit=False) # 받아온 값들을 저장 - commit=False는 바로 저장하지 말라는 것
            post.author = request.user # 저자 = 글을 쓴 사람(유저)
            post.published_date = timezone.now() # 글을 쓴 시간 = 지금 시간
            post.save() # 저장버튼 - 실제로 이 때 db에 저장이 된다.
            return redirect('blog:post_detail', pk=post.pk) # redirect 메서드 호출해서 post_detail로 연결 - 즉 글쓰고 저장완료시 post_detail화면으로 이동하라는 뜻

    else: # request에서 가지고 있는 메서드가 POST가 아니면 (GET이면)
        form = PostForm(instance=post) # instance=post를 넣음 - 즉 비어잇는 폼에 post를 담음
    return render(request, 'blog/post_edit.html', {'form': form}) # render함수를 리턴, post_edit.html을 리턴 및 form 변수에 form을 할당