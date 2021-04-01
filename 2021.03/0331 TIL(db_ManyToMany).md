# 0331 TIL

1:N 으로 모델링 만들어보기

프로젝트 만들어서

1)) models.py에 이렇게 추가하자.

```
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()

    def __srt__(self):
        return f'{self.pk}번 환자 {self.name}'
```

1:N => 의사가 1, 환자가 N

2)) 환자가 N이니까 `doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)` 추가하기

3)) makemigrations, migrate 해주기

4)) shell_plus => 

```
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: doctor2 = Doctor.objects.create(name='eric')

In [3]: patient1 = Patient.objects.create(name='tony', doctor=doctor1)

In [4]: patient2 = Patient.objects.create(name='harry', doctor=doctor2)
```

1번환자가 1번의사가 마음에 안 들어서 2번의사에게 진료를 받고 싶어함. => 방문예약을 바꾸는 것은 불가능. 새로운 객체를 만들어야 함.`In [6]: patient3 = Patient.objects.create(name='tony', doctor=doctor2)` => 이것이 1:N의 한계점

다른 의사에게 방문한 기록은 어떻게?? / 방문예약을 1에서 2 의사로 변경하려면??? => 중개모델을 작성해보자! (의사와 환자의 pk 값을 가지고 있는 중개 모델을 만들어보자!) => 외래키 지우고 shell_plus도 꺼서 모델 수정하기!

(사진 - 2.중개모델)

5)) models.py 수정하기!

```
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor_id}번 의사 {self.patient_id}번 환자'
```

6)) 데이터 초기화하기

`db.sqlite3` 지우고, hospitals의 migrations에서 0으로 시작되는 파일 다 지우기

7)) makemigrations / migrate

8)) shell_plus

```In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: patient1 = Patient.objects.create(name='tony')

In [3]: doctor1
Out[3]: <Doctor: 1번 의사 justin>

In [4]: patient1
Out[4]: <Patient: 1번 환자 tony>

In [5]: Reservation.objects.create(doctor=doctor1, patient=patient1)
Out[5]: <Reservation: 1번 의사 1번 환자>
```

9)) 생성은 끝! 이제 조회를 해보자!

의사 입장에서 예약을 조회하는 것은 역참조! => doctor가 reservation을 참조하는 거니까

```
In [6]: doctor1.reservation_set.all()
Out[6]: <QuerySet [<Reservation: 1번 의사 1번 환자>]>
```

환자 입장에서 예약 조회하기 => patient가 reservation을 참조 = 역참조

```
In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사 1번 환자>]>
```

10)) 

```
In [8]: patient2 = Patient.objects.create(name='harry')
# 2번 환자 만들기
In [9]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[9]: <Reservation: 1번 의사 2번 환자>
# 1번 의사에게 예약 추가
In [10]: doctor1.reservation_set.all()
Out[10]: <QuerySet [<Reservation: 1번 의사 1번 환자>, <Reservation: 1번 의사 2번 환자>]>
# 의사가 확인해보니 환자 2명 있음
```

for문으로도 확인할 수 있다.

```
In [11]: for reservation in doctor1.reservation_set.all():
    ...:     print(reservation.patient.name)
    ...: 
tony
harry
```

(사진)

지금 이렇게 한 것.

11)) many to many 필드 작성 => 복수형으로 적어야 함.

`doctors = models.ManyToManyField(Doctor)` => foreignkey와 똑같이 작동

12)) class reservation(중개모델)은 주석처리하기 => 다시 데이터 초기화

13)) makemigrations / migrate => sqlite explorer에서 확인해보니 3개가 만들어짐(`hospitals_patient_doctors` 가 생겼다.) => 얘를 열어보니 중개모델과 똑같다.

14)) 매니투매니필드 : 중개테이블을 자동으로 만들어준다!

아까처럼 중개테이블을 거치는 것이 아니라 서로를 바로 참조할 수 있게 되었다.

(사진 - MTM 필드작성)

15)) shell_plus => `In [6]: patient1.doctors.add(doctor1)` 이렇게하면 환자가 직접 의사를 추가했다. 현재 주체가 환자이기 때문에.

16)) 조회

```
In [7]: patient1.doctors.all()
Out[7]: <QuerySet [<Doctor: 1번 의사 justin>]>
```

17)) 의사의 입장에서 조회해보기 => 역참조(나를 참조하고있는 필드를 가진 애를 참조하는 것) 정확히 개념을 말하자면 무조건 1이 N을 참조하는게 역참조가 아님.

```
In [8]: doctor1.patient_set.all()
Out[8]: <QuerySet [<Patient: 1번 환자 tony>]>
```

18)) 어디에 두든 중개테이블은 만들어지기 때문에 매니투매니필드는 편한 곳에 만들어도 된다.

의사가 환자 등록하기 `In [9]: doctor1.patient_set.add(patient2)` => 안에 명령어만 바뀐다. 역참조니까!

이렇게 되면 이제 환자가 2명이다.

```
In [10]: doctor1.patient_set.all()
Out[10]: <QuerySet [<Patient: 1번 환자 tony>, <Patient: 2번 환자 harry>]>
```

19)) 예약취소하기 => 의사가 취소하기 `In [11]: doctor1.patient_set.remove(patient1)`  / 환자가 취소하기 `In [13]: patient2.doctors.remove(doctor1)`

20)) doctor.patient_set.말고, doctor.patients를 쓰고 싶다. 역참조 모델 이름을 바꾸고 싶다. => `related_name`

`doctors = models.ManyToManyField(Doctor, related_name='patients')` 이렇게 수정하기 => makemigrations, migrate 해주기

21)) 다시 shell_plus => related_name을 사용하면 이제는 _set은 사용 불가!

(사진 - related name)

매니투매니필드 : 두개의 테이블이 변하는 것은 없다. / M:N은 우리가 판단해서 모델링을 해야한다. 서로 참조가 가능하기 때문에! 모델링하기 어려움...

---

:bear: ManyToManyField()

- M:N 관계를 나타내기 위해 사용하는 필드
- 하나의 필수 위치 인자(M:N 관계로 설정할 모델 클래스)가 필요
- 필드의 RelatedManager를 사용하여 관련 개체를 추가(add), 제거(remove) 또는 만들 수 있음

:bear: Related manager

- 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저

- methods 

  - :exclamation: 같은 이름의 메서드여도 각 관계(1:N, M:N)에 따라 다르게 동작

  - 1:N 에서는 :exclamation: target 모델 객체만 사용 가능

    (관계필드를 갖고있는 모델 : 소스모델(외래키 갖고있는애), 그걸 참조하는게 타겟모델) -> 다시 제대로 찾아보기

  - M:N 에서는 관련된 두 객체에서 모두 사용 가능

  - add(), remove(), create(), clear(), set() (여기서 add랑 remove가 중요)

:bear: ManyToManyField's Arguments(인자)

- 모두 optional하며 관계가 작동하는 방식을 제어
- related_name
- symmetrical
- through(중개모델을 직접 만들 때 사용)

:honey_pot: related_name

- 타겟 모델이 소스 모델을 참조할 때 사용할 manager name
- ForeignKey의 related_name과 동일
- source model (instance)
  - 관계 필드를 가진 모델(외래키나 ManyToManyField를 가진 모델)
- target model(instance)
  - 소스 모델이 관계 필드를 통해 참조하는 모델

:honey_pot: symmetrical (재귀) -> MantToManyField가 재귀적으로 작성될 때만 사용된다.

사진 넣기

```python
from django.db import models

class Person(models.Model):
	friends = models.ManyToManyField('self')  # 클래스 자기 자신을 다시 참조(self)
```

- 위처럼 동일한 모델을 가리키는 정의의 경우 Person 클래스에 person_set 매니저를 추가하지 않음(역참조에 관련된 매니저가 추가되지 않는다.)
- 대신 대칭적(symmetrical)이라고 간주하며, source 인스턴스가 target 인스턴스를 참조하면 참조받은 target 인스턴스도 source 인스턴스를 참조하게 됨
- self와의 M:N 관계에서 대칭을 원하지 않는 경우 symmetrical를 False로 설정(아무 것도 안 쓸 때가 True) -> 난 널 팔로우했는데 넌 아직 난 팔로우하지 않았어!(이 때가 대칭이 아닐 때)

:honey_pot: through

- django는 다대다 관계를 관리하는 중개 테이블을 자동으로 생성함
- 하지만, 중개 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- :exclamation: 일반적으로 추가 데이터를 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용(=추가데이터를 활용한 중개테이블을 사용할 경우)

:bear: Related manager's methods in Many To Many Relationship

:honey_pot: add()

- 지정된 객체를 관련 객체 집합에 추가
- 이미 존재하는 관계에 다시 사용하면 관계가 복제되지 않음(1번 의사에 2번 환자가 예약했는데, 또 1번 의사에 2번 환자를 예약시킨다? 이럴 때는 또 할 수 없다.)

:honey_pot: remove()

- 관련 객체 집합에서 지정된 모델 객체를 제거(관계를 끊는다.)

:bear: DB Representation(데이터베이스에서의 표현)

- django는 M:N 관계를 나타내는 중개 테이블(intermediary join table)을 만듦
- 테이블 이름은 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성됨

:bear: 중개 테이블 필드 생성 규칙

:honey_pot: source model 및 target model이 다른 경우

- id
- `<source_model>_id`
- `<target_model>_id`

:honey_pot: ManyToManyField가 동일한 모델을 가리키는 경우

- id
- `from_<model>_id`
- `to_<model>_id`

---

### Like

:monkey_face: Article과 User의 관계에서 살펴보자! (ManyToMany)

08번 열어서 가상환경 설정하기!!

1)) articles models.py => 

이름짓기 : `article.~~~.all()` => 이 게시글의 좋아요를 누른 모든 유저를 조회. 
저 '~~~'을 like_users로 지어보자!

2)) `like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)` 를 class Article에 추가하기 -> 유저모델을 참조하니 `settings.AUTH_USER_MODEL`를 적는 것.

3)) makemigrations를 하니까 역참조(Reverse accessor)에서 충돌이 된다고 에러가 뜬다. 왜??

현재 User와 Article이 2가지 관계를 맺고 있다. 기존에는 1:N, 지금은 M:N

1:N -> `article.user.~~` / `user.article_set.~~~` 이렇게 참조

M:N -> `article.like_users.~~` / `user.article_set.~~` 이렇게 하는데 user.article_set.이 똑같아서 이게 문제이다.

1:N 에서  `user.article_set.~~~` 의 역할은 유저가 작성한 모든 게시글, M:N에서는 좋아요를 누른 모든 게시글. => 역할이 다르다! => 그래서 방법은 둘 중의 하나를 바꿔줘야 한다.

=> 그래서 `like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')` 이렇게 realted_name을 추가해주기! -> 보통 이런 경우에는 1:N쪽 보다는 M:N쪽에서 바꾼다.

 다시 makemigrations / migrate 해주기

4)) like 구현하기! => articles의 urls.py => `path('int:article_pk>/likes/', views.likes, name='likes'),` 추가하기

5)) views.py

```python
@require_POST  # db에 변경방식이 생기기 때문에 get으로 들어오면 안된다.
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
	# 내가 '좋아요를 누른 사람들 리스트 안'에 있으면
    if request.user in article.like_users.all():
    	# 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 좋아요 누름
        article.like_users.add(request.user)
    return redirect('articles:index')
```

6)) index.html에 추가

```html
<div>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %} <!--views.py에서 적은 조건과 같음!-->
      <button>좋아요 취소</button>
    {% else %}
      <button>좋아요</button>
    {% endif %}
  </form>
</div>
```

7)) 서버 돌려서 회원가입한 후 게시글 작성 => 좋아요 버튼 누를 수 있음!

8)) views.py => 로그인한 사용자만 좋아요 누를 수 있게 likes  함수 맨 위쪽에 `if request.user.is_authenticated:` -> `return redirect('accounts:login')`

9)) 좋아요 버튼 몇 명이 눌렀는지 => index.html => `<p>{{ article.like_users.all|length }}명이 이 글을 좋아합니다.</p>` 추가



---

웹엑스

shell_plus

In [2]: Article.dummy(5)

p1 = Person.objects.get(id=1)

p2 =  Person.objects.get(id=2)

a1 = Article.objects.get(id=1)

a2 =  Article.objects.get(id=2)

p1.article_set.add(a1) -> p1이 a1을 좋아요 표시함

a2.likes.add(p1) -> a2에 p1이 좋아요 표시

아 좋아요 잘못 누름... => p1.article_set.remove(a1) / a2.likes.remove(p1) => 어차피 같은 결과. 누구 입장에서 얘기를 하냐임.

p3 = Person.objects.get(id=3)

a1.likes.add(p3)

a1.likes.add(p1, p2)

a1.likes.all() -> 나를 좋아하는 사람 모두 보여줘

a1.likes.count() -> 나를 좋아하는 사람 수

a1.likes.filter(name='Michael') 

a1.likes.filter(name__contains='Michael') -> 그 중 마이클이라는 이름을 가진 사람 찾기

p3.article_set.all()  -> p3가 좋아하는 게시글 보여줘



models.py => `scraps = models.ManyToManyField(Person)` 스크랩 할 거임. => 내가 스크랩한 게시글을 보고 싶을때에도 `p1.article_set.all()`이 되어버림. 겹친다! => likes 에 related_name을 추가한다. `related_name='likes'`/ scraps에도 `related_name='scraps'` 추가하기. likes랑 scraps 이름도 바꾸기 -> likers, scrapers ====> 교수님 코드 확인

Aritlcle이 Person을 부를 때 likes라고 부르는 것이고, Person이 Article을 부를 때 related_name을 부르는 것이다.

저장 후 makemigrations / migrate 하기(board만)

shell_plus => Article.dummy(5) => Person.dummy(5) 



p1 = Person.objects.get(id=1)

p2 = Person.objects.get(id=2)

p3 = Person.objects.get(id=3)

p4 = Person.objects.get(id=4)

a1 = Article.objects.get(id=1)

a2 = Article.objects.get(id=2)

a3 = Article.objects.get(id=3)

a4 = Article.objects.get(id=4)

a1.likers.add(p1, p2, p3, p4)

p1.likes.add(a1, a2, a3, a4)

p3.scraps.add(a1, a2, a3, a4)

a1.likers.all()

a2.scrapers.all()



person이 article을 작성하는 구조가 되었다.

`author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='my_articles')` Article에 추가하기 => 우리는 무조건 person=....(Person) 으로 해야하는 줄 알았다. 근데 이름 바꿀 수 있다.  related_name을 작성하지 않으면 이름이 겹쳐서 불가능하다. 

`editor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='edit_articles')`  /  `dislikers = models.ManyToManyField(Person, related_name='dislikes')`  => 이렇게 다 추가 가능

서버사이드에서 고민해야 할 2가지 1) 모델링 / 2) 쿼리

---

라이브

views.py =>쿼리셋에서 filter를 걸어서 생각해보자! =>  `if article.like_users.filter(pk=request.user.pk<현재 요청하는 유저의 pk>).exists():` 와 `if request.user in article.like_users.all():` 는같다. => exists가 하는 일은 무엇인가? -> 필요한 정보 하나만 갖고와서 검사한다.(그 전에는 all을 이용해 유저 정보 전부를 갖고왔었다.) 

exists() : 쿼리셋에 특정 결과가 포함되어 있으면 True를 반환, 그렇지 않으면 False를 반환 -> 왜 씀? 가능한 가장 빠른 방법. -> 언제씀? 쿼리셋이 커질 수록 그 특정 하나를 검색하는데에 유용하다.

=> 쿼리셋을 잘 알면 이해가능하다. 

exists는 전체 조회가 필요하지 않을 때 사용한다. 우리가 지금 필요한 게 있는지 없는지 정도만 확인하는 것. 근데 지금 우리가 만드는 것들은 그리 큰 사이즈가 아니라 둘 다 사용해도 상관없음

---

### Follow

:monkey_face: 보통 팔로우 버튼은 유저의 프로필 페이지에 있기 때문에 프로필 페이지를 만들자!

accounts(어디에 만들어도 상관은 없지만, 유저의 프로필이니까 게시글보다는 accounts에 더 관련이 있는 것 같아서 여기에 만들자!) ->  urls.py => `path('<username(앞의 str 생략 가능)>/', views.profile, name='profile'),` 입력

views.py => update_session_auth_hash 뒤에 `get_user_model` 추가(같은 위치에 있으니까!) / `get_object_or_404()`도 import 받기

```python
def profile(request, username):
	# user라고 하면 헷갈리니까. 장고에서 context로 넘겨줄 수 있는 기본 값 중에 하나라서 헷갈림. 그래서 user 쓰지 않기!
	person = get_object_or_404(get_user_model()<user를 참조하는 함수>, username=username)
    context = {
    	'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

:monkey_face: profile.html 생성

```html
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<hr>
<h2>{{ person.username }}'s 게시글</h2>
<!--유저가 작성한 모든 게시글 출력하기-->
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
 <div>{{ comment.content }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}'s likes</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

:monkey_face: 메인페이지 네브바 같은 곳에 '내 프로필로 가기'를 만들고 싶다.

base.html => 로그인한 사용자에게만 보이도록! => `{% if request.user.is_authenticated %}` 안에다가 => `<a href="{% url 'accounts:profile' request.user.username %}">[내 프로필]</a>`  => 로그아웃을 하게되면 '내 프로필'이라는 링크는 사라지게 된다.

:monkey_face: 작성자를 눌렀을 때 작성자의 프로필로 가기!

index.html => :exclamation::exclamation: ​여기서  주의사항 : ` <a href="{% url 'accounts:profile' request.user.username %}"></a>` 이렇게 적어주면 request.user.username 때문에 로그인한 나의 프로필로만 가게 된다. 그럼 안된다. 우리는 다른 사람들의 이름을 누르면 그 사람의 프로필로 가도록 할 것! => 

그래서 request.user.username이 아니라 article.user.username이어야 한다. => < b>작성자 : `<a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a><b>`  이렇게 적자!

---

:monkey_face:  본격적으로 follow 기능 구현하기

follow는 user와 user를 연결 -> articles보다는 accounts가 낫다.

1)) accounts => models.py => 우리는 어차피 User를 수정해야 해서 accounts를 수정하는 것이 좋다. -> 유저대체작업(처음에 `class User(AbstractUser):`)을 한 뒤로 한 번도 User모델을 사용하지 않았었는데 이제 여기에 추가로 수정할 것. 처음에 유저대체작업을 하지 않고는 앞으로 할 과정을 할 수 없던 것이었다. 그래서 처음에 유저대체작업을 하라고 했던 것. 

=> `form django.contrib.auth.models import AbstractUser` -> 이미 되어 있었음 

:exclamation: 요즘 SNS는 비대칭관계인 경우가 많다.(인스타에서 팔로워와 팔로우의 숫자가 다름! 내가 누구를 팔로우 한다고 해서 그 사람이 나를 자동으로 팔로우하지 않음!) => symmetrical은 기본값이 True인데, True이면 대칭관계이다.(내가 친추하면 서로 친구 관계가 되는 것) => 근데 요즘은 비대칭이니 symmetrical을 False로 줘서 꺼버리자!

:exclamation: 대칭일 때는 역참조가 발생하지 않는다. -> 어차피 한 명이 참조를 하면 같이 참조하기 때문에!

:exclamation: 비대칭일 때는 역참조가 발생한다. 그러니 symmetrical을 꺼버리면 related_name이 필요하다!

```python
class User(AbstractUser):
	followings = models.ManyToManyField('self', symmetrical=-False, related_name='followers') # 그냥 참조할 때는 followings, 역참조할 때는 followers
	# 재귀 참조는 self
```

2)) 모델에 변경사항이 생김 => makemigrations / migrate

3)) 중개 테이블 확인하기!(sqlite.explorer에서) 이제 ManyToManyField이니 중개테이블이 생긴다. 

accounts_user_followings => from_user_id / to_user_id -> 만약 참조를 한 게 자기 자신이라면 from_user_id, to_user_id로 방향 설정을 해준 것. 

from_user_id | to_user_id
          1            |           2
          2            |           1

지금 이 상황이 서로 맞팔로우를 한 상태이다!

1 ---> 2 이렇게만 되어 있다면 혼자만 팔로우한 상태.

만약 symmetrical이 True라면 1 ---> 2로 되어있어도 자동으로 맞팔이 되어버린다!

4)) urls.py => `path('<int:user_pk>/follow', views.follow, name='follow')`

5)) views.py => 아까 라이크와 크게 다르지 않다.

```python
@require_POST  # 중개테이블에 데이터가 들어가는 형식이기 때문에 get 방식은 부적절하다.
def follow(request, user_pk):
	# 팔로우 받는 사람
	you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    # 나 자신은 팔로우 할 수 없다.
    if you != me:  
        if you.followers.filter(pk=request.user.pk).exists():
        # if request.user in person.followers.all(): 
            # 팔로우 끊음(너의 followers에서 나를 지움)
            you.followers.remove(me)
        else:
            # 팔로우 신청
            you.followers.add(me)
    return redirect('accounts:profile', you.username)
```

follow는 두 개의 인스턴스가 필요.(팔로우 받는 사람 / 팔로우 요청하는 사람)

```
if person.followers.filter(pk=request.user.pk).exists():
# if request.user in person.followers.all(): 
```

--> 저 사람을 팔로우하는 사람 중에 내가 이미 있다면? 이라는 뜻  : 근데 전체 쿼리셋이 필요 X. 내가 있는지 없는지만 알면된다!
만약에, person의 followers들 중에 내 pk랑 같은 사람이 있는지 없는지(exists) filter로 판단 

:question: 왜  get이 아니라 filter를 쓸까? => get은 우리에게 쿼리셋을 주는애가 아니다. 즉, 값이 없으면 does not exists가 발생. 에러발생. filter는 값이 없으면 빈 쿼리셋, 있으면 있는 쿼리셋을 리턴한다. 즉 있든 없든 쿼리셋을 준다.

:exclamation: follow의 주의사항 : 반드시 남을 팔로우해야한다. 나 자신을 팔로우할 수 없다. 그래서 전체를 진행하기 전에 내가 당신과 다른 사람이어야 한다. => `if you != me:`

6)) profile.html에 팔로우 기능 구현하기

```html
<h1>{{ person.username }}님의 프로필</h1>

<div>
 <div>
   팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
 </div> 
 {% if request.user != person %} <!--로그인한 유저(요청한유저)와 프로필주인이 다를때만! 같으면 내 프로필이니까 그 때는 팔로우 버튼이 보이면 안된다.-->
   <div>
     <form action="{% url 'accounts:follow' person.pk %}" method="POST">
       {% csrf_token %}
       {% if request.user in person.followers.all %}
     	<button>언팔로우</button>
       {% else %}
         <button>팔로우</button>
       {% endif %}
     </form>
   </div>
</div>
```



7)) views.py => follow도 좋아요와 마찬가지로 인증된 사용자만 접근하도록 설정한다.

```python
def follow(request, user_pk):
	if request.user.is_authenticated:
		...
	return redirect('accounts:login')
```

:exclamation: 팔로우가 좋아요와 다른 점 : 좋아요는 내 글에 좋아요를 누를 수 있지만, 팔로우는 그래서는 안된다. 그래서 내가 팔로우하려는 사람이 나와 다른 사람인지를 확인하고 진행해야 한다!



:exclamation: manytomany는 팔로우 팔로잉이 헷갈려도 상관없다. 어차피 서로가 서로를 참조하기 때문에 바껴도 동작하는건 똑같다.(재귀이기 때문에=자기 자신이기 때문에)
종속관계가 아니기 때문에 from과 to의 방향이 헷갈려도 상관 X -> 중요한 건 내가 참조할 때는 뭐로 불리고, 역참조할 때는 뭐로 불린다를 알아두는 것!



:dancer: 장고의 공식 진도는 여기서 끝!!!!!!!!!!!! :dancer:

---

### 참고사항들

:monkey_face: 템플릿에서  `person.followings.all`랑`person.followers.all`이 너무 자주 쓰여서 변수로 만들고 싶다!

그럴 때는 with를 사용하기!

```html
{% with followings=person.followings.all followers=person.followers.all %}
	...
{% endwith %}
```

:exclamation: with와 endwith 안에서만 저 변수를 사용할 수 있다!



:monkey_face: in을 안 쓰고 왜 exists를 쓰는가?  -> 이를 알기 위해서는 쿼리셋 api에 대해 얘기를 해야함

```python
if you.followers.filter(pk=request.user.pk).exists():
# if request.user in person.followers.all(): 
```

lazy(게으름) : 쿼리셋은 게으르다. 는 문구를 쿼리셋api를 검색했다면 장고 공식문서나 블로그 등에서 발견할 수 있었을 것.

:banana: 왜 쿼리셋은 lazy 한가?? => 실제 쿼리셋을 만드는데에는 데이터베이스의 작업이 포함되지 않는다.

쿼리셋을 만드는 것 자체에는 orm이 db에 요청을 보내지 않는다. 그럼 언제 보내는데? -> 평가를 할 때. 그럼 평가는 언제하는데? -> print로 출력할 때 
평가를 한다 : 쿼리를 db로 날린다. / 쿼리셋 캐시를 만든다.

평가를 하기 전까지는 db가 관여를 하지 않는다.

:exclamation: 평가가(쿼리를 db로 날리는 시점이) 언제인데??? => 쿼리셋에 해당하는 db의 레코드들을 실제로 가져오는 것을 평가라고 한다. 
1)) 반복될 때 :heavy_check_mark:
2)) 슬라이싱될 때
3)) repr() 객체표현 --> 이게 print()  :heavy_check_mark:
4)) len() 길이 잴 때
5)) bool() --> if문  :heavy_check_mark:

```python
q = Entry.objects.filter(title__startswith="What")
q = q.filter(created_at__lte=datetime.date.today())
q = q.exclude(context__icontains="food")
print(q)
```

이렇게 되면 3번 db요청을 보내는 것 같지만, 실제 요청은 한 번만 이루어진다.(print할 때)

:banana: Iteration : 반복할 때

쿼리셋은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행(평가)한다.
쿼리를 보냈다는 건 평가가 되었다는 것.

```python
for e in Entry.objects.all(): # 이렇게 했을 때 평가가 한 번 이루어졌다.
	pass
```

:banana: bool()

```python
if Entry.objects.filter(title__'test'): # if 선언했을 때 평가가 된다.
	pass
```

:exclamation: 평가가 되면 쿼리셋의 내장 캐시에 저장된다. ==> 우리가 쿼리셋을 다시 순회할 때 그 때 또 평가를 하는게 아니라 이미 평가된 내장 캐시를 재사용한다.

:banana: Caching and QuerySets

```python
# 나쁜 예
print([e.headline for e in Entry.objects.all()]) # 평가
print([e.pub_date for e in Entry.objects.all()]) # 평가

# 좋은 예
queryset = Entry.objects.all()  # 쿼리셋을 미리 만들어놓고 얘를 사용. 이렇게 만드는것 자체는 db에 어떠한 영향도 끼치지 않는다.
print([p.headline for p in queryset]) # Evaluate the query set. (평가)
print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation. (캐시에서 재사용)
```

:banana: When QuerySets are not cached (근데 항상 캐시가 되는 건 아니다)

쿼리셋의 특정 요소에 접근할 때는 캐시로 못 넣는다.

```python
# 캐시 되지않는 경우
queryset = Entry.objects.all()
print(queryset[5]) # Queries the database 
print(queryset[5]) # Queries the database again
# 쿼리셋의 특정 요소 인덱스에 접근함. 이러한 경우는 두 번 평가가 된 것.
```

```python
# 위 상황을 방지하고 싶을 때
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database (전체 쿼리셋을 평가 시켜버림)
print(queryset[5]) # Uses cache
print(queryset[5]) # Uses cache
# 그 다음에는 사용을 해도 캐시가 된다.
```

:question: 왜 이렇게 하는거야..? => 데이터를 최적화 시키려고!!
최적화 : 보다 적은 쿼리로 원하는 데이터를 얻는 과정

:banana:우리의 LIKE 코드를 예시로 사용해보자

```python
like_set = article.like_users.filter(pk=request.user.pk)
if like_set: # 평가
    # 쿼리셋의 전체 결과가 필요하지 않은 상황임에도
    # ORM은 전체 결과를 가져옴
    article.like_users.remove(request.user) 
```

```python
# 개선 1
# exists()는 쿼리셋 캐시를 만들지 않으면서 특정 레코드가 있는지 검사
if like_set.exists():
    # DB에서 가져온 레코드가 없다면
    # 메모리를 절약할 수 있다
    article.like_users.remove(request.user)
```

```python
# 만약 IF 문안에서 반복문이 있다면?

# if에서 평가 후 캐싱
if like_set:
    # 순회할때는 위에서 캐싱된 쿼리셋을 사용
    for user in like_set:
        print(user.username)
```

```python
# 만약 쿼리셋 자체가 너무너무 크다면??
# iterator()
# 데이터를 작은 덩어리로 쪼개서 가져오고, 이미 사용한 레코드는 메모리에서 지움
# 전체 레코드의 일부씩만 DB에서 가져오므로 메모리를 절약
if like_set:
    for user in like_set.iterator():
```

```python
# 그런데 쿼리셋이 너무너무 크다면 if 평가에서도 버거움
if like_set.exists():
    for user in like_set.iterator():
        pass
```



:exclamation: exists나 iterator 메서드를 활용하면 메모리는 최적화할 수는 있지만, 쿼리셋 캐시는 생성되지 않기 때문에 또 db 쿼리가 중복이 될 수 있다.
메모리 자체는 아낄 수 있지만 아래쪽에서 또 다시 같은 쿼리가 반복될 여지가 있다.

--> 자칫 잘못하면 안일한 최적화가 될 수도 있다는 것을 주의하라!