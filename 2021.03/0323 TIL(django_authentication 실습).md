# 0323 TIL

어제 했던 거에서 추가로 살을 붙일 것!

네브바를 추가할건데, base.html이 너무 길어진다...

그래서 templates에 _navbar.html을 만들어 여기에 따로 빼주기! _ 달려있는 애들은 부품이라는 뜻! 

그 대신 base.html에 `{% include '_navbar.html' %}` 적어주기

_navbar.html 수정하기(코드 참조하기)

{{ user }} 는 {{ user.username }}과 같다.

여기서 중요한 건 {% if user.is_authenticated %} 이걸 쓴다는 것. 로그인 했을 때 안 했을 때 다르게 보여주는데, is_authenticated를 사용하는구나를 알아야한다.

<a class="nav-link {% block index %}{% endblock index %}" 이렇게 block을 넣어서 index.html에도 {% block index %}active{% endblock index %} 이렇게 해주면 Home을 눌렀을 때 그 글씨가 검은색이 됨(New도 눌렀을 때 검은색 됨) => 근데 이건 지금 우리가 navbar를 부품으로 사용해서 안된다... base.html에 직접 네브바를 넣었을 때는 가능하다.

---

articles의 views.py => 이거 추가해주고 더 튼튼하게 만들기

```
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
```

new 함수에 추가하기(이 둘의 순서가 중요하다)

```
@login_required
@require_http_methods(['GET', 'POST'])
```

---

accounts의 urls.py에 `path('profile/', views.profile, name='profile'),` 추가 => index path는 지우고, views.py에서도 index를 profile로 고쳐서 쓰기

```
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {'user_profile': user_profile}
    return render(request, 'accounts/profile.html', context)
```

---

profile.html 만들기

```
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

---

forms.py에 `class CustomUserChangeForm()`를 만들고 위에 `UserChangeForm` 추가 => `User = get_user_model()` 이렇게 저장 후

```
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
```



---

views.py => 맨 위에  `CustomUserChangeForm` 추가 => profile 함수 => `form = CustomUserChangeForm()` 랑 context에 `'form': form,` 추가



---

회원탈퇴

urls.py에 `path('withdraw/', views.withdraw, name='withdraw'),` 추가 => 얘는 나만 탈퇴시킬 수 있기 때문에 username을 추가하지 않아도 된다.

views.py에 추가

```
@login_required
@require_POST
def withdraw(request):
    request.user.delete()  # 팔찌를 차고 있는 사람을 없앤다.
    auth_logout(request)  # cookie(팔찌) 회수 + session 테이블에서 레코드 삭제
    return redirect('articles:index')
```

profile.html에 button에 ` onclick="return confirm('진짜 하실건가요?ㅠㅠ')` 추가

---

비밀번호 바꾸기

urls.py에 `  path('profile/password/', views.change_password, name='change_password'),` 추가

views.py에 AuthenticationForm 뒤에 `PasswordChangeForm` 추가

---

settings.py에  `AUTH_USER_MODEL = 'accounts.User'
어떤 역할?
얘는 그냥 선언문.
1) djangoPJt는 단 1개의 사용자 관리 모델만 활성화 가능
2) 사용자 관리모델의 조건 == AbstractUser라는 모델을 상속받은 모델
3) django.contrib.auth.models 모듈 내부에 User 모델이 기본값
4) 현재 settings.py 에서는 안보이지만, 무대뒤에서 settings.AUTH_USER_MODEL을 확인하면, 'auth.User'라고 나온다.
5) 하지만, 우리는 직접 만든 커스텀 사용자 관리 모델(accounts.models.User)을 사용할 것이다. => 확장 가능성 때문에
6) 이 5번에 대한 선언이 아래줄과 같다.
AUTH_USER_MODEL = 'accounts.User'  => accounts.models.User 지만, 이렇게 작성한다.
그래서 models.py에 User를 만들어줘야 함. => from django.contrib.auth.models import AbstractUser
를 해주고 클래스를 만들어주면 사용자 관리 모델이 만들어지는 것. 근데 일단 지금 우리는 안 필요해서 pass -> 나중에 필요하면 추가



UserCreationForm는 save가 끝나면 본인을 return한다.

---

settings.py에 등록 및 세팅하고, forms.py랑 models.py 적어주기

urls.py에 적어주기(싸인업, 로그인, 로그아웃, 프로필까지 다)

views.py에 함수 틀(싸인업, 로그인, 로그아웃, 프로필까지 다) 만들기 => signup은 user create, profile은 user read  / 이거랑 별개로 login은 session create, logout은 sesson delete이다. 

사인업 : fron .forms import CustomUserCreationForm => if request.method == 'post': => form = CustomUserCreationForm(request.Form) => if form.is_valid(): => form.save() 세이브는 user를 리턴하니까 user=form.save() 교수님은 new_user라고 함. 상관없음 => else: => form = CustomUserCreationForm() => context = {'form': form,} => return render(request, 'accounts/signup.html', context) => is_valid는 return redirect('accounts.signup')

signup.html => extends => block =>h1 SIGNUP h1 => form method="POST" => csrf_token => form.as_p => button 회원가입 button

profile 함수(detail과 같음) => 원래는 get_object..404 이거 해야하는데 안해도 되는건 팔찌차고 들어왔으니까! 팔찌 찬 건 어떻게 알아? login_required로 막을거니까! 데코레이터 추가하고,  me = request.user(요청을 보낸사람이 나다.) => context = {'me': me} => return render(request, 'accounts/profile.html', context)

profile.html =>  extends => block =>h1 profile h1 => {{ me.username }} 끝!

login, logout 함수 불러오기 => signup 함수에 new_user 밑에 auth_login(request, new_user) 뉴유저한테 팔찌 채워줄거니까

서버 돌리면 사인업에 모든 내용이 다 튀어 나온다. 왜? 폼에 fields.가 all이니까, 그래서 유저네임만 받자고 변경하기

password는 내가 추가 안햇는데? 그래도 알아서 나오는게 이 모델폼의 역할이다.

로그인 -> AuthenticationForm은 모델폼이 아니라서 form.save가 들어가지 않는다. 이게 auth_login()으로 바뀐 것. 이 함수를 실행하고 return redirect => else: 평소랑 똑같음.

기존유저가 form.save가 아니라(이미 있는걸 찾았으니까 id/pw에 매칭하는 사용자를 추출했으니까!) auth_login이 있는 것.(세션 테이블에 추가 + 팔찌차는 것)   => 얘도  2개 인자가 필요함. request, old_user 이게 규칙 old_user는 아까 기존유저.

AuthenticationForm은 첫번째 인자가 무조건 request. 이게 규칙이다!!

로그인.html은 싸인업.html 복붙하기



로그아웃 auth_logout(request) => return redirect('accounts:login')