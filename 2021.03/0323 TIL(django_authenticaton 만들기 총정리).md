# 0323 signup, login, logout, profile 정리

1)) 빈 폴더 만들어 이름 설정 후 코드로 열기

2)) `python -m venv venv` => `source venv/Scripts/activate` => ctrl+shift+P => Python select interpriter => Python 3.8.7 64-bit ('venv')

3)) `pip install django django_extensions` => `pip freeze > requirements.txt` => `touch .gitignore` => gitignore 설정하기

4)) `django-admin startproject 프로젝트이름` => `python manage.py startapp 앱이름` => settings.py에 앱이랑 django_extensions 등록 => BASE_DIR 설정 => `AUTH_USER_MODEL = 'accounts.User'` 작성

여기서 AUTH_USER_MODEL = 'accounts.User'는 사용자 관리 모델을 사용하기 위한 선언문. 사용자 관리 모델의 조건은 AbstractUser라는 모델을 상속받은 모델이다. 이 모델은 django.contrib.auth.models 모듈 내부에 있는 User 모델이 기본값이다.

5)) 그래서 models.py에 User 만들기 => `from django.contrib.auth.models import AbstractUser` 선언 => `class User(AbstractUser):` => 이렇게 클래스를 만들어주면 사용자 관리 모델이 만들어진다. => `address = models.CharField(max_length=100)` 클래스 안에 이런식으로 추가 가능. pass도 가능

6)) forms.py 만들어서 적어주기 => 

```python
# User 생성/수정은, *비밀번호* 때문에 생성과 수정이 나눠졌다.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

# 생성담당: UserCreationForm <=> auth.User(default User) <=> 수정담당: UserChangeForm 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )
        # 이 때 보통 fields = '__all__'이라고 했는데 회원가입때도 이렇게 하면 진짜 오만가지 정보를 다 입력하라고 한다... 귀찮... 그래서 유저네임만 받자고 변경했다.
```

모델이랑 폼 작성하고 makemigrations, migrate 해줘야 할 듯

---

7)) 프로젝트 urls.py에 적기 => 앱 urls.py에 적기(싸인업, 로그인, 로그아웃, 프로필까지 다) + 앱 네임도 

8)) views.py에 일단 함수 틀 만들기(싸인업, 로그인, 로그아웃, 프로필까지 다)
signup은 User table Create / profile은 User table detail이고, 이것과 다르게 login은 Session table Create / logout은 Session table Delete이다.

9)) signup부터 시작! 그 전에 `from .forms import CustomUserCreationForm` 추가 => signup은 CustomUserCreationForm을 사용한다는 것을 잊지 말자! => 그래서 이 함수의 구조를 살펴보면, POST로 받을 때와 GET으로 받을때는 나누며, form은 CustomUserCreationForm으로 받는다. => form 유효성 검사를 하고, 유효하다면 저장을 한다. 이 때 변수명 지정하기(아무거나 상관없지만 회원가입이기 때문에 새로운 회원이 온다는 것을 알아두자) => login 함수를 사용하기(왜? 너 인증됐어! 라고 팔찌 채워주는 역할.)(앞으로 def login이 등장하기 때문에 이름을 바꿔주자 auth_login으로) login 함수를 사용하기 위해 선언하기(`from django.contrib.auth import login as auth_login`) => 그 다음 return redirect하기 => 이번에는 GET일 때를 보면, form은 빈 폼으로 들어온다. => context와 return render는 POST일 때 유효성 검사에서 통과하지 못한 경우에도 받아야 하기 때문에 내어쓰기를 한다. 이 때 우리는 render해서 accounts/signup.html로 갈 것

10)) signup.html로 가준다고 했으니 만들어주자! => extends, block => 제목 만들기 => form 태그 사용. 여기서 action은 필요없다. POST로 받을 것 =>안에 내용 채우고 button 만들어주기

---

11)) views.py에서 profile 함수 만들기 => 원래는 article = get_object_or_404(Article, pk=article_pk) 이렇게 특정 객체를 불러오지만, 요청을 보낸 사용자는 request.user로 바로 가져 올 수 있다. profile 확인은 로그인 한 당사자만 할 수 있기 때문에. => `me = request.user` 라고 해주자. 직접 로그인한 당사자이기 때문에 me로! => context, return render 해주기(accounts/profile.html로!)

=> 여기서는 일단 프로필을 보는것만 만들었다. 회원수정은 또 다르다.

12)) profile.html 생성 => extends, block, 제목 => {{ me.username }} 끝!
근데 여기서, `{{ me.username }}`을 사용해도, `{{ user.username }}`를 사용해도,`{{ request.user.username }}`를 사용해도 모두 같은 값이 나온다. 이 셋의 차이는 무엇일까? 일단, me=request.user라고 했으니 첫번째와 세번째는 같다. 그리고 첫번째와 두번째는 결과는 같지만 좀 다른데, user는 html 작성 시 사용되는 장고 문법(DTL)의 예약어로, user라는 문자 자체가 의미하는 것이 현재 요청을 보낸 사용자라는 것.

아니 그럼 05_AUTH_2에서 views.py의 def profile의 주석은 뭐지? 그건 위에 보면 `user = get_object_or_404(User, username=username)`라고 해서 user는 username이라고 지정, 근데 여기서 헷갈리니까 context로 'user_profile' : user라고 해줬다. 그래서 username을 의미하는 user는 user_profile인 것.

user가 요청한 사용자라는 것은 html에서 쓰이는 예약어라고 생각하자!

헷갈릴 수 있음ㅠㅠㅠ

이거는 반 친구가 답변해준 말! 

셋 다 같은 말이기는 합니다! 1. me는 views함수에서 랜더 함수의 인자로 들어간 context에 포함되어 있는 me로, views 함수에서 request.user 로 정의되어있습니다. 즉, 현재 요청을 보낸 사용자입니다. 2. user는 DTL(html 작성 시 사용되는 장고 문법)의 예약어 입니다. 파이썬의 from, True 와 같이 문자 자체가 의미를 갖는 것이 예약어입니다. DTL에서 user를 사용할 경우 현재 요청을 보낸 사용자를 의미합니다. 3. request.user는 요청을 보낸 사용자를 의미합니다. 요청 자체를 render 함수를 통해 인자로 받았기 때문에 이렇게 쓸 수 있는 것...일 겁니다. 즉 전부 다 '요청을 보낸 사용자'라는 뜻이에요

---

13)) views.py에 login 함수 => 이것도 회원가입과 같은 맥락으로 흘러간다. POST로 들어왔을 때 => 근데 여기서는 form을 AuthenticationForm을 사용하기 때문에, `from django.contrib.auth.forms import AuthenticationForm` 를 선언해줘야 한다. => 이 폼은 사용자가 제출한 id/pw가 올바른지(=User DB에 있는지) 검증한다. 이 폼의 규칙은 첫번째 인자가 무조건 request라는 것. 그래서 request, request.POST 이렇게 사용한다. => 유효성 검사. 검증이 올바르게 끝나면, id/pw에 매칭하는 사용자 추출이 가능하다. => 기존 유저의 정보를 갖고와 old_user라는 변수에 저장. `old_user = form.get_user()` => 여기서는 form.save()를 하지 않는다. (왜? 모델폼이 아니기 때문에!) 대신 `auth_login(request, form.get_user())`을 한다.(이 로그인 함수도 첫번째 인자에 무조건 request) 너 로그인 됐어! 라고 팔찌 채워주기 이게 session 테이블에 추가하면서 팔찌 채워주는 역할이다. =>  그 다음 return redirect하기 => GET으로 들어왔을 때 => form을 받는다. 빈 폼을 받을 때에도 이 폼은 무조건 첫번째 변수가 request여야 한다. => context, return render 하기(내어쓰기)

14)) login.html은 signup.html 복붙하자. 제목만 다르다. 아, 버튼 이름만 변경하면 될 듯

---

15)) views.py에서 def logout 적어주기 => 얘는 logout()만 쓰면 되는데 일단 logout() 함수를 불러와주고, 이름도 변경한다. `from django.contrib.auth import logout as auth_logout` => `auth_logout(request)` => 그 다음 return redirect하면 끝. 로그아웃하면 login 페이지로 돌아가거나, 메인화면으로 돌아가게 해주면 된다. 지금은 메인화면을 안 만들어서 그냥 로그인 페이지로 가도록 설정했다.

16)) 페이지를 더 튼튼하게 만들기! => 

```python
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
```

그 다음 각 함수 위에 데코레이터를 추가한다. => signup, login에 `@require_http_methods(['GET', 'POST'])` 적기

---

:bear: 회원 수정

1)) accounts의 urls.py => `path('profile/', views.profile, name='profile'),` 추가 => index path는 지우기

2)) views.py에서도 index를 profile로 고쳐서 쓰기

```python
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {'user_profile': user_profile}
    return render(request, 'accounts/profile.html', context)
```

3)) profile.html 만들기

```html
{% extends 'base.html' %}
{% block content %}
<h1>{{ user_profile.username }}</h1>
{% comment %} 
  /accounts/profile/neo
  => user_profile = <User: neo> 객체 
{% endcomment %}
{% comment %} request.user -> 지금 화면을 보고있는 사람 {% endcomment %}
{% if request.user == user_profile %}
<div>
  <form action="" method="POST">
    {% csrf_token %}
    개인정보 수정 <input type="text">
    <button class="btn btn-primary">정보 수정</button>
  </form>
  <form action="#" method="POST" class="d-inline-block">
    {% csrf_token %}
    <button class="btn btn-danger">회원 탈퇴</button>
  </form>
</div>
{% endif %}
{% endblock content %}
```

button은 form 안에서는 input type submit과 같고, form 밖에서는 아무 기능 없는 버튼이다.

4)) forms.py =>  `class CustomUserChangeForm()`를 만들고 위에 `UserChangeForm` 추가 => `User = get_user_model()` 이렇게 저장 후

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
```

5)) views.py =>  맨 위에  `CustomUserChangeForm` 추가 => profile 함수 => `form = CustomUserChangeForm()` 랑 context에 `'form': form,` 추가

---

:bear: 회원 탈퇴

1)) urls.py => `path('withdraw/', views.withdraw, name='withdraw'),` 추가 => 얘는 나만 탈퇴시킬 수 있기 때문에 username을 추가하지 않아도 된다.

2)) views.py => 

```python
@login_required
@require_POST
def withdraw(request):
    request.user.delete()  # 팔찌를 차고 있는 사람을 없앤다.
    auth_logout(request)  # cookie(팔찌) 회수 + session 테이블에서 레코드 삭제
    return redirect('articles:index')
```

3)) profile.html => button에 ` onclick="return confirm('진짜 하실건가요?ㅠㅠ')` 추가

---

:bear: 비번 변경

1)) urls.py =>  `  path('profile/password/', views.change_password, name='change_password'),` 추가

2)) views.py =>  AuthenticationForm 뒤에 `PasswordChangeForm` 추가

앞에서 사용했던 UserChangeForm으로는 비밀번호 수정이 불가능하다. 비밀번호는 암호화가 되어 DB에 저장되기 때문에 단순히 User edit form에서 알아볼 수 있는 문자로는 수정이 불가능하며 암호화 괒엉이 필요하다. 따라서 비밀번호 변경을 위한 별도의 폼을 사용해야한다. => 그게 django 내장 폼인 PasswordChangeForm이다.

3)) change_password 함수 만들기

```python
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/change_password.html', context)
```

4)) change_password.html 만들기

```html
{% extends 'base.html' %}
{% block content %}
<h1>Change Password</h1>

<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button class="btn btn-warning">Set Password</button>
</form>
{% endblock content %}
```

5)) profile.html => 비밀번호 변경 링크 달기

```html
<div>
  <a href="{% url 'accounts:change_password' %}">비밀번호 변경</a>
</div>
```

6)) views.py

세션에는 비밀번호를 포함하여 유저의 정보가 담겨있다. 비밀번호가 바뀔 경우, 기존의 세션에 담긴 유저의 비밀번호와 일치하지 않게 되고, 세션이 만료되어 로그인이 풀리게 된다. 따라서 비밀번호를 변경하고도 로그인을 유지하게 하기 위해서는 추가적인 코드 작성이 필요하다.

`update_session_auth_hash(request, form.user)`

:세션에 있는 로그인 정보 해쉬를 업데이트 할 때 사용하는 메서드
:새로 설정된 비밀번호의 정보는 user에 담겨있다.
:request 인자를 통해 session에 정보를 업데이트한다.
:사용을 위해 import 해와야 한다.

```python
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            from django.contrib.auth import update_session_auth_hash  # 교수님은 여기에 import 하심.. 왜? 맨 위에는 안되나?
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/change_password.html', context)
```

