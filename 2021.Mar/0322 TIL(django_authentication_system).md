# 0322 TIL(Authentication System)

:bear: Authentication & Authorization

:honey_pot: Authentication

- 인증
- 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

:honey_pot: Authorization

- 권한, 허가

- 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정

:bear: Django Authentication System

- 일반적으로 authentication system(인증 시스템) 이라고 함

---

05번 복사해와서

새로운 앱 만들기 => accounts 라는 이름으로 => 앱 등록한 후 urls.py 적기(from import, app_name, urlpatterns 틀만) => 프로젝트 urls.py도 적기 => migrate 해주고 서버 열어보기(articles로) => 잘 작동하면 일단 ok

---

:bear: Authentication in Web requests

- Django는 세션과 미들웨어를 사용하여 인증 시스템을 request 객체에 연결
- 이를 통해 사용자를 나타내는 모든 요청에 request.user를 제공
- 현재 사용자가 로그인하지 않는 경우 AnonymousUser 클래스의 인스턴스로 설정되며, 그렇지 않으면 User 클래스로 설정됨

:bear: 로그인

- 로그인은 Session(이하 세션)을 Create하는 로직과 같음

:honey_pot: login()(django가 미리 제공)

- 현재 세션에 연결하려는 인증된 사용자가 있는 경우 login() 함수로 로그인 진행
- request 객체와 User 객체를 통해 로그인 진행
- Django의 session framework를 통해 사용자의 ID를 세션에 저장

:bear: 로그아웃

- 로그아웃은 세션을 Delete 하는 로직과 같음

:honey_pot: logout()

- request 객체를 받으며 return이 없음
- 현재 요청에 대한 DB의 세션 데이터를 삭제하고 클라이언트 쿠키에서도 sessionid를 삭제

:bear: HTTP(HyperText Transfer Protocol)

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 약속)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트 - 서버 프로토콜
- 요청(requests)
  - 클라이언트(브라우저)에 의해 전송되는 메시지
- 응답(responses)
  - 서버에서 응답으로 전송되는 메시지
- HTTP 특징
  - 비연결지향(connectionless)
    - 서버는 응답 후 접속을 끊음
  - 무상태(stateless)
    - 접속이 끊어지면 클라이언트와 서버 간의 통신이 끝나며 상태를 저장하지 않음 => 네이버 메인페이지 로그인 후 뉴스탭으로 이동. 이 때 로그인이 풀리나? ㄴㄴ => 근데 이 무상태에 의하면 로그인이 풀려있어야 함. 그래서 결국은 이 상태를 계속 유지시켜야 함. 이를 위해 쿠키라는 개념이 등장

:bear: Cookie(쿠키)

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 브라우저(클라이언트)는 전송 받은 쿠키를 로컬에 key-value의 데이터 형식으로 저장
  - 동일한 서버에 재 요청 시 저장된 쿠키를 함께 전송
- 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 로컬에 저장하고, 클라이언트가 재요청시마다 웹 페이지 요청과 함께 쿠키 값도 같이 전송

:honey_pot: 쿠키 사용 목적

- 세션 관리(상태를 저장) : 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리 (중요!!)
- 개인화 : 사용자 선호, 테마 등의 세팅
- 트래킹 : 사용자 행동을 기록 및 분석하는 용도

:bear: Session(세션)

- 사이트와 특정 브라우저 사이의 "state(상태)"를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 session id를 쿠키를 사용해 저장, 클라이언트가 다시 서버에 접속할 때 해당 쿠키(session id가 저장된)를 이용해 서버에 session id를 전달

  HTTP 특징 2개 때문에 쿠키가 있는 것.

- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라오저와 사이트가 연결된 세션을 알아냄.(세션 정보는 django DB의 django_session 테이블에 저장)

- 주로 로그인 상태 유지에 사용

:bear: Cookie lifetime(라이프타임, 일생)

:honey_pot: Session cookie

- 현재 세션이 종료되면 삭제
- 브라우저는 현재 세션이 종료되는 시기를 정의
- 일부 브라우저는 다시 시작할 때 세션 복원(session restoring)을 사용해 계속 지속될 수 있도록 함

:honey_pot: Permanent cookie(영구적인 쿠키)

- Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제

쿠팡에 물건을 장바구니에 담은 후 개발자도구에서 application에서  sid라는 데이터를 삭제하고 새로고침하면 장바구니가 비어있게 된다.
장바구니의 상품을 내가 페이지를 이동할 때마다 장바구니의 물건을 계속 요청한다.

:bear: Cookie & Session

:honey_pot: Cookie 

- 클라이언트 로컬에 파일로 저장

:honey_pot: Session

- 서버에 저장
- 이 때 서버에 저장된 세션데이터를 구별하기 위한 sesson id는 쿠키에 저장

"HTTP 쿠키는 상태가 있는 세션을 만들도록 해준다."

---

로그인 로그아웃 구현해보기

1)) urls.py에 로그인 적기

2)) views.py => login 함수 적기 => 맨 위에 `from django.contrib.auth.forms import AuthenticationForm` 추가 => login 함수에서 GET일 때 login 문서를 보내니까 login 문서 먼저 적어주기!

```
else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

지금 빌트인 폼을 사용하기 때문에 forms.py를 만들지 않는다.

3)) templates/accounts 폴더 만들고, login.html 만들기 => 만든 후 서버 열기

![image-20210322111203476](0322 TIL(django_authentication_system).assets/image-20210322111203476.png)

4)) 다시 views.py로 가서 이번에는 POST 부분을 적어보자(무조건 이 순서로 적어야 한다.) POST부분은 아래가 작성되고 나서 적어야 한다.
=> `form = AuthenticationForm(request, request.POST)` 얘는 첫번째로 무조건 request를 받고 그 다음에 request.POST를 적는다. => if valid 다음은 세션이 create 되어야 한다. => 위에 `from django.contrib.auth import login` 추가 => `login(request, form.get_user())`을 적는데, login  함수와 지금 적은 것과 이름이 겹침. 그래서 수정하기 => 그리고 위에 import login 뒤에 as auth_login 추가하기

```
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 통과 후 세션이 CREATE 되어야 한다.
            # login(request, form.get_user())
            auth_login(request, form.get_user())
```

5)) python manage.py createsuperuser 로 아이디와 비번을 만들어주고, 다시 서버를 돌린 후 로그인 페이지에 이 아이디와 비번을 넣고 제출하면 => 로그인 페이지가 유지되면서, 개발자 도구에서 application을 보면 sessionid가 추가된다. 

(근데 난 로그인이 안 됨. 제출 누르니까 에러뜬다....ㅠ)

6)) sqlite를 열어주고 django_session을 열어보면 session_key가 저장된다. 장고는 세션에 대한 데이터를 쿠키가 아니라 데이터베이스에 저장한다.

7)) 우리가 아까 POST인 경우 return 값을 안 넣어줘서 `return redirect('articles:index')` 을 추가.

8)) base.html에 `<h3>Hello, {{ request.user }}</h3>` 추가 => articles 사이트로 접속하면, 우리가 아까 로그인했기 때문에 Hello, 로그인한 아이디가 나온다. => 로그인한 상태가 아니면 Hello, AnonymousUser라고 뜬다. 

---

새 프로젝트 만들기

1)) 가상환경이랑 장고랑 다 설치하고 기존의 article  앱 갖고오기 `$ cp -r ../03_FORM/articles/ .` => ignore도 갖고오기 `$ cp ../04_STATIC_MEDIA/.gitignore .`

2)) accouts라는 앱 만들기(사용자인증 때는 accounts 앱으로 하는게 국룰)

3)) templates도 갖고오기 `$ cp -r ../03_FORM/templates/ .`

4)) settings.py에 세팅하기

5)) 프로젝트 urls.py에 path 적기 

6)) 일단 articles가 제대로 돌아가는지 확인하자

7)) accounts에 urls, forms 만들고, templates/accounts/index.html login.html signup.html 만듦

8)) 그 다음 서버 돌리니까 오류 => migrate 안 해줌 => makemigrations 해주고, migrate 해주기 (articles 만!!!) => 서버돌리기(근데 난 왜 또 오류뜨냐...)

9)) settings.py 맨 밑에 `AUTH_USER_MODEL = 'accounts.User'`  적기

10)) models.py에 적어주고

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username, password, is_active, is_staff,... etc columns가 들어가있다.
    address = models.CharField(max_length=100)
```

11)) makemigrations랑 migrate해주기(accounts)

12)) sqlite 열어주기

![image-20210322135105373](0322 TIL(django_authentication_system).assets/image-20210322135105373.png)

맨 밑에 우리가 추가한 address가 있다. 그 앞에는 원래있는  columns가 있음

13)) `python manage.py migrate` 하기.(이번에는 다 migrate 해주기)

14)) forms.py => 지금은 일단 여기까지 적기

```
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # little customize
    class Meta:
        model = 
```

---

라이브

1)) settings.py에 이것을 입력하는데 그냥 session_cookie_age = 86400이라 하지 말고, 86400이 무엇을 의미하는지 변수를 지정해서 의미를 적어주기

```
DAY_IN_SECONDS = 86400
SESSION_COOKIE_AGE = DAY_IN_SECONDS
```

주석으로 남겨도 상관없음. 팀의 가이드에 따라 다르다.

2)) 앱의 url에 작성하기

3)) views.py => 맨 위에 from import로 logout 함수 불러오기(얘도 이름 겹치니까 바꿔주기) => logout 함수 적어주고, decolator 주기

---

로그인/비로그인에 대한 제한 걸어보기

- is_authenticated => attribute(속성)
- login_required => decorator

:bear: is_authenticated attribute

- User에 항상 True이며, AnonymousUser에 대해서만 항상 False
- 단, 이것은 권한(permission)과는 관련이 없으며 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

---

4)) base.html에 if, elif, else 넣기

5)) views.py에서 POST 확인 전에 로그인햇는지부터 확인

```
if request.user.is_authenticated:
        return redirect('articles:index')
```

6)) articles의 index.html => 

```
{% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
```



---

:bear: login required decorator

- 사용자가 로그인 했는지 확인하는 view를 위한 데코레이터
- 로그인 된 사용자의 경우 해당 view 함수를 실행
- 로그인 하지 않은 사용자는 setting.LOGIN_URL에 설정된 경로로 redirect 시킴
  - LOGIN_URL의 기본 값은 '/accounts/login/'

---

7)) aritlces의 views.py => `from django.contrib.auth.decorators import login_required`

8)) create 함수 위에 @login_required => 이렇게 되면 로그인 하지 않으면 create 누르면 자동으로 login 화면으로 redirect 하게 된다.

9)) delete와 update 위에도 `@login_required` 를 붙여주기 => 얘네들 다 로그인해야만 할 수 있는 동작이기 때문에

10)) accounts의 views.py에서 login 함수에 POST일 때 return을 `return redirect(request.GET.get('next') or 'articles:index')` 이거로 체인지

11)) 넥스트파라미터를 인식하지 못한다면 login.html의 form action 값 비워주기(?ㅠㅠ)

12)) 비로그인 상태로 강제로 지우려고 시도했더니 login_required 때문에 로그인 화면으로 옴. => 그럼 여기서 로그인하면 글이 지워져야 한다. => 그래서 로그인하면 405에러가 뜬다. => 그래서 login_required를 지우고 

```
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')
```

이렇게 수정하자.

웹 리퀘스트에 대한 인증 끝...!

---

회원가입부터 하기!

C

1)) accounts의 urls.py에 추가(signup)

2)) accounts의 views.py에 signup 함수 만들어주기

```
def signup(request):
    if request.method == 'POST':
        pass 
    else:
        pass
```

구조는 항상 같다.

3)) views.py 맨 위에 `UserCreationForm` 추가하기 => else 부분에 밑에 추가하기

```
else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



4)) signup.html 만들기 => login.html이랑 똑같아서 복붙하고 이름만 회원가입으로 바꿔주기

5)) 서버 돌리기 => 이렇게 하니까 회원가입에 대한 설명이 나온다.

6)) base.html => else 밑에 로그인 밑에 `<a href="{% url 'accounts:signup' %}">Signup</a>` 추가

7)) views.py => signup 함수

```
if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
```

signup 함수 중 맨 위에 추가

```
if request.user.is_authenticated:
	return redirect('articles:index')
```

---

R은 패스! D가 간단하니 D부터 하자!

회원탈퇴시키기

1)) urls.py 먼저 작성

2)) views.py에 delete 함수 추가

```
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```

3)) delete 함수도 decolator 사용 => `@require_POST`

4)) base.html에 로그아웃 밑에 추가

```
<form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="탈퇴">
</form>
```

5)) 실제 탈퇴버튼 눌러본 후 admin 페이지가서 확인해보기

---

U 회원정보수정

1)) urls.py 적고, views.py에 update 함수 만들어주기 => 얘도 빌트인 함수를 사용할거라 맨 위에 `UserChangeForm` 추가하기

2)) update.html 만들고 signup.html 복붙해서 이름만 수정

3)) base.html => if 바로 밑에 `<a href="{% url 'accounts:update' %}">회원정보수정</a>` 추가

4)) 서버 돌려보니 회원정보수정 페이지에 뭔가 굉장히 많이 뜬다.

5)) accounts 앱에 forms.py 생성 => 

---

:bear: User objects

- django 인증 시스템의 핵심
- django 인증 시스템에서는 오직 하난의 User Class만 존재
- AbstractUser Class의 상속을 받음
- AbstractUser 
  - User Model을 구현하는 완전한 기능을 갖춘 기본 클래스

User는 직접 참조하지 않는다. 그래서 우리는 get_user_model()로 작성한다.

---

6)) forms.py에

```
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

7)) views.py 맨 위에 `from .forms import CustomUserChangeForm` 추가하기 => update 함수에 else 부분에 `form = CustomUserChangeForm()` 로 수정

8)) update 함수 POST일 때 채워주기

```
if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
```

9)) 서버 돌려서 제출 누른 후 admin 사이트에서 확인해보기

10)) 로그인 상태에서만 회원정보 수정 가능하도록 하기 위해 맨 위에 `from django.contrib.auth.decorators import login_required` 추가하고, update 함수에 @login_required 추가하기 => else 밑에 form에도 instance 추가하기

---

:bear: User 참조

:honey_pot: get_user_model() method

- User를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 user model을 참조해야 함
- 현재 프로젝트에서 활성화 된 user model을 return
- 커스텀한 user model이 있을 경우에는 커스텀 user model, 그렇지 않으면 User를 참조

---

1)) forms.py에

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    # little customize
    class Meta:
        model = get_user_model()
        여기에 fields = '__all__' 하면 회원가입할 때 엄청나게 많은 정보를 다 입력해야함
```

2)) views.py에 `from .forms import CustomUserCreationForm` 추가하고 signup 함수 채워주기

```
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

3)) signup.html에 추가

```
{% extends 'base.html' %}
{% block content %}
<h1>SIGN UP FOR FREE</h1>
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock content %}
```

4)) 서버 돌려보면 회원가입 시 어마어마한 정보를 입력해야 한다. 그래서 forms.py를 수정하자 => fields = ('username',)

5)) views.py에 redirect랑 `from django.contrib.auth.forms import AuthenticationForm` 추가

`from django.contrib.auth import login as auth_login`

`from django.contrib.auth import logout as auth_logout` 얘네도 추가

6)) login 함수 채워주기

```
def login(request):
    # login 검증 / HTML 만드는 forms.Form을 써서 완료
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야 하는데...
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)
```

7)) urls.py에 login 추가 logout도 추가

8)) index도 추가하고, index 함수도 추가해준다.

9)) views.py에 from django.contrib.auth import get_user_model 추가하고, index 함수 위에 `User = get_user_model()` 추가하기

10)) 회원가입했더니 회원목록이 뜨는데 지금 내가 로그인 한 상태가 아니라고 뜸. => signup 함수에 유효성검사에 `auth_login(request, user)` 추가.  => 다시 회원가입 해보면 제대로 됨.