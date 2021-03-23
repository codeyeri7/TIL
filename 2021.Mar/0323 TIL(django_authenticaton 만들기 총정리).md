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
근데 여기서, `{{ me.username }}`을 사용해도, `{{ user.username }}`를 사용해도,`{{ request.user.username }}`를 사용해도 모두 같은 값이 나온다. 이 셋의 차이는 무엇일까? 일단, me=request.user라고 했으니 첫번째와 세번째는 같다. 그리고 첫번째와 두번째는 결과는 같지만 좀 다른데, request.user는 `/profile/<username>`으로 요청을 보낸 사람이고(로그인 한 당사자), user는 `/profile/<username>`에서 username에 해당하는 사람(내가 다른 사람 프로필 볼 수 있는 경우, 그 프로필의 주인)이다. 

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

회원수정, 비밀번호 변경, 탈퇴는 추가로 다시 정리하기!