# 0324 TIL

:clapper:

:bear: Relationship fields

:honey_pot: 모델 간 관계를 나타내는 필드

- Many to one (1 : N)
  - ForeignKey()
- Many to Many (M : N)
  - ManyToManyField()
- One to One (1 : 1)
  - OneToOneField()

:bear: A many-to-one relationship in RDBMS

:honey_pot: Foreign Key(외래키) : 자식이 부모 테이블을 참조하기 위해 저장한 부모 테이블의 PK를 말한다.

- RDBMS에서 한 테이블의 필드 중 다른 테이블의 행(row)을 식별할 수 있는 키

- 참조하는 테이블에서 1개의 키에 해당하고 이는 참조되는 측의 테이블의 기본 키를 가리킨다
- 하나의 테이블이 여러개의 외래 키를 포함할 수 있다
  - 그리고 이러한 외래키들은 각각 서로 다른 테이블을 참조할 수 있다
- 참조하는 테이블의 행 여러개가, 참조되는 테이블의 동일한 행을 참조할 수 있다(댓글 여러개가 한 개의 게시글과 연결)

- 참조하는 테이블과 참조되는 테이블이 동일할 수도 있다(재귀적 외래 키) -> 대댓글
- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성) => 데이터의 정확성과 일관성을 유지하고 보증하는 것이 데이터 무결성인데 그 3가지 중 하나
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일해야 함(여기에 부합하는 건 pk가 가장 정확하다)

:bear: 데이터 무결성의 3가지를 장고에서 어떻게 사용하는가?

:honey_pot: ForeignKey()

- django에서 A many-to-one relationship(1:N)을 표현하기 위한 model field
- 2개의 필수 위치 인자가 필요
  1. 참조하는 모델 클래스
  2. on_delete 옵션

```python
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

:bear: on_delete

- ForeignKey가 참조하는 객체가 사라졌을 때 ForeignKey를 가진 객체를 어떻게 처리할 것인지를 정의 (게시글이 사라졌을 때 거기에 달린 댓글을 어떻게 처리할 것인가)
- 데이터 무결성을 위해서 매우 중요한 설정이다
- 데이터 무결성 : 데이터의 정확성과 일관성을 유지하고 보증하는 것

:bear: on_delete의 옵션 7가지

- CASCADE : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
- PROTECT : 참조가 되어있는 경우 오류 발생
- SET_NULL : 부모 객체가 삭제 됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건 시 불가능)
- SET_DEFAULT : 모든 값이 DEFAULT 값으로 치환
- SET() : 특정 함수 호출
- DO_NOTHING : 아무것도 하지 않음
  - 다만, 데이터 베이스 필드에 대한 SQL ON DELETE 제한 조건을 설정해야 한다.
- RESTRICT(new in 3.1)

중요한 것은 1번째 : CASCADE / 나머지는 이런게 있다 정도로만 알아두면 된다.

---

풀 받아서 거기에 작성(06)

댓글 모델 구현

articles의 models.py => `class Comment(models.Model):` 작성 =>  밑에 추가 한 후

```python
content = models.CharField(max_length=200)  # 보통 댓글은 글자 제한이 있으니까
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

ForeignKey 추가하기(맨 위에) => `article = models.ForeignKey(Article, on_delete=models.CASCADE) # on_delete의 속성 중 지금은 CASCADE만 기억하자`

그 밑에 이것도 추가

```python
def __str__(self):
    return self.content
```

아티클 클래스와 다른 것 : 제목이 없고, 외래키가 있다.

`makemigrations` 해주기 => 그럼 0002가 생김 => `migrate` 해주기 => db 열어보기(aritlce:aritlce) 이걸 열어보면 얘는 그대로. 댓글에 관련되어서는 어떠한 것도 들어있지 않다. => articles_comment 를 보면 마지막에 외래키의 필드가 article_id로 만들어졌다. => models.py에 적었던 class 변수의 이름인 article에 id를 더한 것.

댓글 작성하기 => `python manage.py shell_plus`=> 인스턴스부터 작성 `comment = Comment()` => 내용 추가 ` comment.content = '댓글1'` => `comment.save()`를 했더니 오류 뜸...(NOT NULL constraint failed: articles_comment.article_id) 댓글의 내용도 저장되어야 하지만, 몇 번 게시글에 작성이 된 건지를 알아야 하는데 지금 그걸 모르겠다고 뜬 것. => 일단 게시글부터 작성하자 `Article.objects.create(title='제목1', content='내용1')` => 그럼 우린 댓글을 일단 작성해놨으니 comment.article_id = article의 pk을 넣어야 한다. => `article = Article.objects.get(pk=1)` 객체를 저장 한 후 => `comment.article = article` 객체 자체를 넣는다. => `comment.save()` 한 후 `comment.pk`를 해보면 1이 나온다.

`comment.article`을 하면 comment가 참조하고 있는 객체가 나온다. pk를 알고 싶을 때 `comment.article_id`를 해주면 1이 나온다. `comment.article.pk`를 해도 똑같이 1이 나온다. *주의사항 : `comment.article_pk`는 안된다. 이런 이름의 column은 없기 때문. article_id라고 정확히 필드명을 지정해줘야 한다.

1번 게시글에 2번째 댓글 달기 `comment = Comment(content='댓글2', article=article)` 인스턴스에 바로 추가하기 => 저장 `comment.save()`하기  => db의 articles_comment를 눌러보면 댓글 2개가 작성된 것을 알 수 있다. 둘 다 article_id는 1번!!

articles.py의 admin.py => 위에 Comment import 받아오고 `admin.site.register(Comment)` 추가하기 => superuser 만들어주기 `python manage.py createsuperuser` => 아이디랑 비번설정(yeri, test1234!) => 서버 돌려서 로그인 한 후  Comments를 눌러서 확인 => 댓글 누르면 변경도 가능!

---

N의 입장에서 1을 참조하는 건 참조 /1의 입장에서 N을 참조하는 건 역참조  => 근데 models.py 코드 구조 상 물리적으로 역참조가 불가능하다(밑에서 위로 참조하는게 구조상 불가능) 이를 도와주는게 model manager

:bear: 1:N model manager

- Comment(N)가 Article(1)을 참조
  - article => `comment.article`

- Article(1)이 Comment(N)를 참조(역참조)
  - comment_set => `article.comment_set.all()`
  - django에서는 역참조시 모델이름_set 형식의 manager를 생성

---

shell_plus에서 역참조를 해보자(이 게시글에 어떤 댓글들이 달렸는지 확인할 수 있음)

`article = Article.objects.get(pk=1)` 1번 게시글 다시 갖고오기 => 

`In [3]: article.comment_set.all()
Out[3]: <QuerySet [<Comment: 댓글1>, <Comment: 댓글2>]>` 이렇게 하면 댓글 2개가 있다는 걸 알 수 있다. 쿼리셋이 나왔다는 것은 얘를 반복해 풀어서 출력할 수 있구나라는 것을 생각해볼 수 있다.

```
In [4]: comments = article.comment_set.all()

In [5]: comments
Out[5]: <QuerySet [<Comment: 댓글1>, <Comment: 댓글2>]>
```

comments라는 곳에 담을 수 있다.

---

:bear: related_name

- Django가 기본적으로 만들어주는 _set manager(역참조 manager)를 변경할 이름 설정
- 1 : N에서는 거의 사용하지 않지만 M : N 관계에서는 반드시 사용해야 하는 상황이 발생

우리가 직접 쳐보지는 않지만 코드 확인하기

`article.comment_set.all()` -> `article.comments.all()`로 바꿔버리는 것. 이렇게 바꾸면 comment_set은 더 이상 쓸 수 없고, comments만 쓸 수 있다. 이렇게 바꾸면 makemigrations랑 migrate 다시 해줘야 함.

---

articles의 forms.py => 댓글 폼 만들기

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment  # Comment를 불어와야 하니 위에 import 하기
        fields = '__all__'  # 일단 어떻게 나오는지 보기 위해 all
```

views.py => detail => `comment_form = CommentForm()` 추가. 그 전에 CommentForm을 import 하기 => 댓글을 작성해야 하니까 빈 폼! => context에 `'comment_form': comment_form,` 추가

detail.html => back 버튼 밑에 추가하기 => 

```html
<form action="#" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

서버 돌리면

![image-20210324103243840](0324 TIL(db).assets/image-20210324103243840.png)

이렇게 나오는데 여기 밑에 Article을 보면 댓글을 쓸 게시글을 선택할 수 있는 건데, 이건 불필요하다. 여기는 이미 1번 게시글의 디테일 페이지이기 때문에. 이 부분은 사용자로부터 받지 않아야 한다. 여기서 사용자에게 받아야 할 부분은 댓글의 내용뿐. 그래서 Article 부분을 빼줘야 한다.

forms.py에서 fields = all을 지우고, `exclude = ('article',)`를 사용해서 전체 중에 article을 제외한다는 것.

---

댓글 작성 시작!

articles의 urls.py => 댓글 내용은 form으로 받지만, 몇번 글의 댓글을 작성할지는 url로 받는다. 그래서 pk로 받음 => `path('<int:pk>/comments/', views.comments_create, name='comments_create'),`  규칙을 정하는 것은 자유이다(comments_create로 정한 것)

detail.html에서 아까 form의 action에 `{% url 'articles:comments_create' article.pk %}` 경로 추가

views.py에 def comments_create 만들어주기!

```python
@require_POST #여기에 데코레이터를 주면 안에서 POST인걸 확인할 필요가 없음
def comments_create(request, pk):  # 얘는 POST만 처리하면 된다. GET은 detail에서 처리함.
    article = get_object_or_404(Article, pk=pk)  # article의 pk가 필요하기 때문에 article 갖고와주기
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
# 기존의 if, else로 돌아가는 큰 구조가 빠짐.(POST만 처리하면 되니까!)
```



서버 돌려서 댓글 작성해서 제출하면 `NOT NULL constraint failed: articles_comment.article_id` 이라는 오류가 뜸 => article_id가 빈 값이야 => 추가적으로 article_id를 받아야한다. url로부터 pk를 받으니 특정 객체의 article을 만든 후 그 article을 입력해줘야 한다. 즉 몇 번 게시글에 작성하는지 넣어야 한다.

그렇기 위해서는 댓글 하나가 인스턴스가 나오게 된다. comment = comment_form.save() 근데 이 인스턴스(comment)는 save를 해야만 나온다. 이미 저장이 되어있는 상태인데, article을 넣고 다시 또 저장하면 이건 생성이 아니라 수정이다. 이렇게 이미 저장이 되어버리면 아래로 갈 수도 없다. 에러가 난다. 왜? 저장하려고 했는데 article_id가 없기 때문에. => 그래서 django는 save에 한 가지 옵션을 제공한다. 그것이 바로 commit!  `comment = comment_form.save(commit=False)` # 이렇게하면 인스턴스는 return 해주는데 db에 저장은 안하고 대기 상태. 이것이 commit=False의 역할 => `comment.article = article` 객체 자체를 넣어주자 => `comment.save()` 저장. 이렇게 하면 article_id도 들어가서 제대로 작동할 것 => 서버 돌려서 댓글 제출하면 당장 페이지가 넘어가지는 않음. 그래서 admin 페이지에서 확인해보자! 그럼 제대로 댓글이 추가된 걸 알 수 있다.

:exclamation: render와 redirect의 차이 다시 확인해보기!(11:05분 부터의 설명 다시 듣기ㅠ)

---

작성한 댓글들 보여주기(댓글 작성란 위에!)

views.py의 detail => `comments = article.comment_set.all()`. 위에 article을 받아온다. detail 페이지에 보이는 현재 게시글에 대한 댓글을 갖고와야 하니까 article.comment_set.all()이 되는 것. => context에 `'comments': comments,` 추가

detail.html => 

```html
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment }}</li>
    {% endfor %}
  </ul>
```

---

댓글 삭제하기

urls.py => `path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),` 추가

views.py => 

```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)  # 맨 위에 Comment 모델 추가하기
    comment.delete()
    return redirect('articles:detail', article_pk) 
    # article_pk를 갖고와야 하는데, 우리가 처음에는 comment_pk만 갖고왔었다.누가 쓴 댓글인지 알기 위해 article_pk를 갖고와야 함
    # urls.py에 article_pk도 추가하기
```

detail.html => 각 댓글 마다 삭제 버튼이 있어야 하니까 li 안에 comment와 같이 나오도록 form 추가

```html
<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
```

댓글 수정은 하지 않겠다. -> 보통은 댓글 수정을 위한 사이트로 이동이 아니라 우리가 있는 페이지에서 그 부분만 수정할 수 있도록 활성화 될 것. 근데 이렇게 하려면 우리가 현재 배운거로는 불가능... 자바스크립트가 필요하다

---

def comments_create(request, pk):  에서 @login_required를 넣을 수 없다. 예를 들어, 얘는 로그인 안 한 사용자가 삭제를 시도했을 때, 로그인 페이지로 보낸다. 근데 문제는 얘의 특성이 next 파라미터를 같이 처리. 그럼 delete로 보낼 때 다시 요청을 보내는데 get으로 보낸다. 그렇게 되면 @require_POST에서 걸려서 405 에러 메세지가 나온다. 이 데코레이터 2개를 같이 쓰고 싶다면, GET으로 처리할 때만!

그래서 `if request.user.is_authenticated:` 를 넣고, 로그인 안 했을 때  login 페이지로 보낸다. `return redirect('accounts:login')`

def comments_delete(request, article_pk, comment_pk):도 `if request.user.is_authenticated:` => 얘는 redirect 필요 없음.

---

댓글 개수 출력

detail.html => ` {{ comments|length }}`  /   `{{ article.comment_set.all|length }}`  /  `{{ comments.count }}` 이 셋 중에 하나를 추가할 수 있다. 근데, commets.count는 안 쓰는게 좋음. 우리는 이 중 첫번째거 사용

---

:bear: Substituting a custom User model (커스텀 유저 모델로 대체하기) -> 오늘 오후 수업의 가장 큰 주제

- 일부 프로젝트에서는 built-in User model이 제공하는 인증 요구사항이 적절하지 않을 수 있음
- django는 custom model을 참조하는 AUTH_USER_MODEL 설정을 제공하여 기본 user model을 재정의(override)할 수 있도록 함 => 기본 유저 모델을 덮어씌우는 것. 그 값을 AUTH_USER_MODEL로 설정
- 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장
- 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
- 단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함*

공식문서( django custom authentication검색 ->  customizing authentication in django 클릭 -> 오른쪽 목차 Substituting a custom User model) 확인

1)) settings.py => `AUTH_USER_MODEL = 'myapp.MyUser'` (앱 이름.유저모델 이름)

2)) accounts => models.py => 유저모델 등록하기

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass # 중간에 커스텀할 여지를 남겨둠
```

왜 AbstractUser를 사용하는가? -> 완전한 기능을 갖춘 사용자 모델을 구현하는 애니까

AbstractBaseUser도 사용가능하지만, 내가 따로 장고가 구동하도록 설정해줘야 한다. 그러니 굳이..?

---

:bear: AUTH_USER_MODEL

- User를 나타내는데 사용하는 모델
- 기본 값은 'auth.User' (settings.py에 가면 auth앱이 깔려있음)
- 주의사항
  - 프로젝트가 진행되는 동안 변경할 수 없음(변경하기 위해서는 많은 노력이 필요) (종속된 모델을 만들고 마이그레이션 된 후)
  - ...

:bear: AbstractBaseUser & AbstractUser

:honey_pot: AbstractBaseUser

- 기본적으로 password와 last_login만 제공
- 자유도가 높지만 필요한 다른 필드는 모두 직접 작성해야 함

:honey_pot: AbstractUser

- 관리자 권한과 함께 완전한 기능을 갖춘 사용자 모델을 구현하는 기본 클래스

:bear: Abstract base classes (tmi 정도로 알아두자)

- 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
- 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우.......서브 클래스의 true 값을 넘겨주는 역할

---

settings.py =>맨 밑에 `AUTH_USER_MODEL = 'accounts.User'` 추가

이제 세팅 끝! 

초기화를 시켜야 함. 왜?? -> `단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함*`

다행히 지금 우리는 데이터가 그리 많지 않음. 해봤자 게시글 2개. 그래서 초기화 시키자.

1)) 모든 설계도 지우기(migrations 폴더에 0으로 시작하는 파일 다 지우기)

2)) db.sqlite3 지우기

3)) 다시 makemigrations, migrate 시키기

확인 상 서버 켜서 회원가입을 해봤더니 `Manager isn't available; 'auth.User' has been swapped for 'accounts.User'` 에러가 뜸. => auth.User가 accounts.User로 바꼈다고 뜸. => 회원가입을 할 수 있는 UserCreationForm은 User라는 모델을 사용한다. 얘는 account.User가 아니라 auth.User이다. 근데 account.User로 바껴서 내가 수행이 불가능하다! 라고 뜨는 것.

이제 우리는 재정의 해줘야 한다. => 공식문서의 `Custom users and the built-in auth forms`로 가보자 => UserCreationForm과 UserChangeForm은 애초에 기본 유저 모델을 참조한 상태로 만들어진 애들이라 어쩔 수 없이 재정의 해줘야 한다. 이 둘만!

accounts의 forms.py => get_user_model이 User를 리턴해준다.(현재 활성화되어있는 함수) 그래서 User라는 이름으로 직접참조하지 말라고 get_user_model을 장고가 만들어놓은 것

맨 위에 UserCreationForm 추가하고 이거 적기

```
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
        # 가입할 때 이메일도 적도록 추가한 것
```

views.py => ` CustomUserCreationForm` import 해주기 => signup 함수에서 `form = UserCreationForm`을  `CustomUserCreationForm`으로 바꿔준다.

=> 서버에서 다시 회원가입을 하면, 이메일주소 입력란도 뜨고 이제는 회원가입이 가능해진다.

---

Article과 Comment간의 관계가 1:N이었는데, 이제는 User가 끼어들 것.

User : Article과 User : Comment 는 둘 다 1:N의 관계이다.

User와 Article(1:N) => 하나의 User는 여러개의 게시글을 가질 수 있다.

articles의 models.py => article class의 맨 위에 `user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)` 추가. 맨 위에 settings도 import 해주기

:bear: Referencing the User model(유저 모델 참조하기)

:honey_pot: settings.AUTH_USER_MODEL  -> 문자열 'accounts.User' 을 반환

- 유저 모델에 대한 외래 키 또는 M : N 관계를 정의할 떄 사용
- 즉, models.py에서 유저 모델을 참조할 때 사용*

:honey_pot: get_user_model()  -> User 객체를 반환

- django는 User 모델을 직접 참조하는 대신 get_user_model()을 사용하여 사용자 모델을 참조하라고 권장
- 현재 활성화된 유저 모델(지정된 커스텀 유저 모델, 그렇지 않은 경우 User)을 반환
- 즉, models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용*

---

공식문서 `Referencing the User model` 로 들어가서 읽어보자 => 유저모델을 참조하는 방법은 딱 2개이다. 

makemigrations하기 => 데이터 추가되었을 때 어떻게 처리할거냐고 물어보고 있다. => foreignkey가 추가될 때 값 뭐로 할거야? => 지금은 게시글 몇 개 없으니까 그냥 1번 유저가 작성한 글로 만들어버리자 => 1번 선택하고, 1 입력 => migrate 해주기

db 열어서 articles_article을 확인하면 foreignkey는 user_id라는 이름으로 만들어졌다. (참조하는 모델의 소문자 단수형으로 이름을 지어야 한다. 그래야 user + id가 합쳐진 것 처럼 이름이 생성됨)

서버를 켜서 create 로 들어가니까 3개의 입력이 뜬다. user -> 너 foreignkey  뭐로 할거야?(내가 작성자인데 작성자 누구로 할거냐는 것) => forms.py로 가자 => 아티클폼의 `fields = ('title', 'content',)` 필드를 이렇게 변경해서 저 두개만 입력할 수 있게 만들자.

---

초스피드로 코드짜기

앱 이름 : board

모델링부터 해야한다.(어떤식으로 구현할 지) => 모델링한 걸 바탕으로 form을 만들고 -> views도 만들고 -> templates도 만든다. 그러니 모델링을 아주 잘 해야 함. 모델을 뒤늦게 바꾸려고 하면 나머지도 다 일일히 바꿔야 함.

1)) models.py =>

```python
class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 공식문서에서 이런식으로 작성하라고 함.
	content = models.CharField(max_length=200) # 여기를 TextField로 하면 html에서 자동으로 textarea가 나온다. 그래서 차필드로.
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
```

2)) urls.py 작성 후 makemigrations board , migrate board

db확인했더니 Comment 클래스의 article이 article_id가 되어있다. 왜? 그냥 자동임

3)) forms.py => `from django import forms` => `from .models import Article, Comment` => class form 써주기 => 추가설정(validation)을 걸어주고 싶다면, class meta위에 달아주기

4)) urls.py => `path('', views.create_article, name='create_article'),` => 이제는 그냥 create라고 적으면 안된다. 같은 urls.py에 comment create, article create 다 들어가기 때문에

comment는 게시글 속의 어떤 댓글이냐 이기 때문에
`/board/1/comments/1/update/`이런식으로  url이 되어야 한다.
=> `path('<int:article_pk>/comments/<int:comment_pk>/update/'),`
f 스트링으로 접두사 넣어주는 것도 가능. 교수님도 한번도 안 해봤지만..

5)) views.py => 함수 틀 만들어주기 => redirect, get_object_or_404 / models와 forms들도 import 해주기

이제는 form이 하나가 아니기 때문에 form = ArticleForm()해주면 밑에서 고생.. 그러니 이름은 article_form이라고 해주자.

index에서 article = Article.objects.all()을 하면 최신 글이 맨 밑으로 간다... 그러니 article = Article.objects.order_by('-updated_at') 이렇게 해서 수정된 순으로 정렬되도록했다.

article_detail 함수가 핵심!

6)) templates에 html 만들기 => create와 update는 form.html로 퉁치기!

form.html => form 태그에 action은 없고, method="POST"

def create_comment에  article = get_object_or_404(Article, pk=article_pk) 지우고, return redirect에서 article.pk대신 article_pk 바로 이렇게 줄 수 있음 그거랑 지금이랑 무슨 차이일까?

NOT NULL 에러 : 비어있을 수 없는 데가 비어있다는 뜻. => save하기 전에 멈춰야 함(라이브 설명 찾아보기)

 

---

역참조 다시 공부하기

순서대로 다시 정리해보고 만들기!!