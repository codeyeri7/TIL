# 0316 TIL(django_form)

저번에 했던 02_MODEL 리뷰

C : html제공하는 단순한 뷰함수 / 제공한 html을 통해 넘어온 데이터를 실제 저장하는 뷰함수

이 중 핵심은 create에 있음.

R : 꼭 두 개가 있을 필요는 없지만 여러개 조회와 단일 조회가 가장 많이 쓰여서 만듦

U : 수정은 생성과 굉장히 유사 => 도우미 html을 주는것 / 핵심 저장 로직

D : 유일하게 하나만 필요 => 도움이 필요없음.

---

new.html에서 form이 제일 핵심 : 이 form 안에서만 일반 사용자가 데이터를 제출할 수 있기 때문. => 특히 POST 방식으로 요청을 보내는 것 더더욱 이 방법밖에 없다.

POST : 사용자가 우리에게 요청을 보내는데, 그 중 90프로는 달라는 요청. 근데 가끔씩은 이것좀 받아가! 라는 방식을 요청할 때 있음(게시글 작성..) 그럼 그 데이터를 받아서 DB에 저장(DB에 변화가 일어남). DB에 변화가 일어날 때는 POST 방식을 써라. http라는 프로토콜의 기획단계에서 이런 경우에는 POST방식으로 요청을 하도록 구분을 해놓자고 만듦. DB의 변화로 인해 망가질 수도 있기 때문에 장고측에서 모든 요청이 전부 거쳐가야하는 middleware를 만듦.(settings.py) -> 이 요청이 이 form에서 제대로 온 게 맞는지 csrf_token을 이용해 안전성을 점검. csrf_token 은 form 안에 있음. 그래서 무조건 사용자에게 같이 날라옴. 그럼 middleware가 어 post 요청이네? 근데 우리가 인증했네?(csrf_token) 그럼 저장-

create뷰함수에서 if post를 안써도 돌았는데 굳이 쓴 이유는 : 요청방식이 post일때만 돌아!라고 한 것. / GET으로 온다면? 우리가 만든 form이 아니라 이상한 사용자들이 get으로 요청을 보내면 우리가 해줄 수 있는게 없으니 다시 작성하러 가라고 한 것. (사람들이 말 안 들을까봐 해놓은 대책)

그것이 약속이니까...ㅎ post를 사용하는 것이다.

---

데이터베이스에 뭔가 잘못을 했다! 시간을 추가하고 싶음. => models.py에 가서 created_at과 updated_at 작성 => auto_now_add : add는 더하다는 얘기니까 생성에 넣어야 함. 생성된 시간을 넣음 , auto_now : 수정된 시간을 넣음

`python manage.py makemigrations orm_practice` 앱 이름 안 써놓으면 앱이 여러개일때 다 적용.(내가 치킨을 먹고 싶어서 앱을 켜서 장바구니에 담아서 결제창까지 옴) => 그랬더니 created_at과 updated_at이 문제가 생길 수 있다고 뜸(어,, 너 잔액이 없어서 아직 결제가 안되는데..?라고 뜬 느낌) => created_at과 updated_at이 생기면 이미 있는 데이터의 시간 자리는 비어있는데 어떻게 할래? 1) 같이 할래? 2) 너가 할래? => 2번 눌러서 내가 다시 수정하기 => `(auto_now_add=True, null=True)` / `(auto_now=True, null=True)` => 비어놔! 라고 하고 싶은데 기본적으로 장고는 이것을 절대 봐주지 않는다.  근데 우리가 null=True를 줘서 이미 있는 데이터에는 빈 값을 허용하겠다는 뜻. => 그 후 다시 `python manage.py makemigrations orm_practice` 를 했더니 아무 문제가 안 뜸. => 근데 우리가 생성된 시간으로 정렬을 하고 싶을 때 에러가 뜰 것.... => null=True 지우고 다시 해보자ㅠ => 이 상태에서 migrate하면 null=True가 그대로 DB에 반영이 될 것이다. => 다시 그 자리에 default=datetime.now()을 추가하기. 그럼 비우지는 않고 지금 시간을 넣는다는 뜻. => 주문서 다시 작성하기! `python manage.py makemigrations orm_practice` => 했더니 default로 값을 준 것에 문제가 있다고 뜸. => auto_now_add도 디폴트값. 이것과 default가 같이 갈 수 없다는 뜻. => default 부분 삭제하기 => 다시 `python manage.py makemigrations orm_practice`를 하고 1번을 눌러서 같이 해결하자고 하고, datetime.datetime.now 로 바꿔달라고 적기. => 점점 꼬여가는데......?ㅠ 걍 처음부터 만들었음 됐을텐데ㅠ => DB를 삭제하자ㅠ `rm db.sqlite3` => `rm orm_practice/migrations/0*` (저 폴더 안에 있는 0으로 시작하는 애를 다 지우겠다) => `python manage.py makemigrations orm_practice` => 0001_initial.py로 새로 작성된다. => `python manage.py migrate orm_practice` ok!!!! 



맨날 이렇게 다 없애고 새로 만들면 되지 뭐하러 수정해요? => 이미 데이터가 10만건이 쌓여있음 어떡해? 이런 경우는 지우는 것 불가 => 지금 개발하는 단계에서는 수정보다는 이렇게 지우는게 제일 빨라서 지금 이렇게 한 것.

---

클라이언트와 서버 사이에는 요청(url)과 응답(문서 한 장)밖에 없다. 여기에 추가하자면, url은 GET과 POST로 온다. 응답도 문서 한 장밖에 없다고 했지만, status code가 필수로 붙어있다.(200, 400, 500..)

2로 시작한 애들은 : 난 성공했다!! 고로 너한테 주고 있다.

3 : redirect와 관련. 

4 : 4와 5는 둘 다 실패인데, 책임소재의 차이가 있다. 4는 책임소재가 client에게 있다.

5는 책임소재가 server에 있다. (서버가 터짐..)

지금 중요한건 status code의 존재



views.py에 맨 위에 redirect 뒤에 get_object_or_404 추가

detail 함수에서 student = get_object_or_404(Student, pk=pk) 적기 -> 이게 student = Student.objects.get(pk=pk)를 대신하는 것. => 이렇게하면 갖고오거나, 404를 내보내거나. 그 동안은 pk값을 이상하게 써서 에러가 뜨면 책임 소재를 server에 줬었다.(500) 근데 이제는 404가 나옴.

이제 앞으로는 모든 student를 이렇게 바꿀 것.

이렇게 없는 pk값을 넣었을 때는 에러가 404가 나와야지!! 라고 알아야 한다.!!

---

내가 models.py를 수정하고 `python manage.py makemigrations orm_practice` 를 하고 migrate를 하면, 0002, 0003만 migration이 된다. => 1번은?? 아까 저장했기 때문에 안 뜸. => 어떻게 알아서 알고 1번은 이미 했고, 2,3번은 안 했었다는 걸 알고 있을까? 1번까지 했다는걸 어디에 저장했을까? => 03에서 db opendata를  하고 sqlite explorer에서 django_migrations를 보면 테이블에 다 저장이 되어있기 때문에!

models.py에서 age를 제한하고 싶다! (3살이 이 글을 쓰지는 않을테니.. 200살두..) => charfiled는 max_length를 썼는데? integerfiled는?? 얘는 () 여기에 안 씀

우리가 name도 5자 이상 못 쓰게 charfiled를 5자로 제한했는데 이게 반영이 안됨. => models에서는 데이터를 제한하기 위한 조건이 아무것도 반영이 안된다. => views.py의 create에서 if len(request.POST.get('name')) <= 5: 를 추가한ㄷ.... => 그럼 여기서 else이면 어떡할거? 다른애들도 일일히 조건을 주어야 하나....? 말이 안 됨...! => 모든 처리를  save()를 실행하기 전에 다 해놔야 한다. 하나라도 내가 원하는 모습과 다르다면 html로 보내야 함.

문제라고 생각되는 부분 

1)) Data Validation 데이터 검증을 어떻게 할 것인가?

edit.html에서 수정햇음...! 확인하기



---

03_FORM 새 프로젝트 시작하기~~~

1)) cp ../02_MODEL/.gitignore . 02모델에 있는 깃 이그노어를 여기로 갖고오겠다

2)) venv

3)) source

4)) pip install django django_extensions ipython 얘네 설치

5)) startproject

6)) select interpreter

7)) startapp

8)) settings.py installed apps = articles, 장고 익스텐션 추가 / BASE_DIR도

9)) models.py => 클래스 Article 작성

10)) 클래스 밑에 

```python
def __str__(self):

  return f'{self.id}: => {self.title}'

# 이걸 추가했으니 migration에 영향을 줄까? 아니 안 줌..
```

ORM은 models.py 내부의 class에서, class var만 확인하여 DB의 Column으로 만든다.

11)) 이제 makemigrations => migrate   : 이거 할 때 꼭 뒤에 앱 이름 써주기! -> 방금 이렇게 써놓고는 막상 실제로 할 때 앱 이름 안씀...ㅠㅠㅠㅠㅠ 제발 좀 기억하고 쓰자!!

12)) `cd articles/` 로 들어와서 `touch urls.py forms.py`

13)) forms.py로 가자 => 맨 위에 from django import forms 적어줌 =>

```python
class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=5)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField()
```

models.py와 매우 유사. 그러나 CharField 안에 옵션이 다름. forms.py에서는 min_length가 있지만 모델에는 없음

---

1)) 프로젝트의 urls.py

2)) 앱의 urls.py

3)) views.py => 맨위에 redirect get_object_or_404  추가 거기에 from import도 추가 => 함수들 추가(일단 전체 틀 만들어주기!)

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm

def new(request):
    return render(request, '')

def create(request):
    return redirect()

def index(request):
    return render(request, '')

def detail(requset, article_pk):
    return render(request, '')

def edit(requset, article_pk):
    return render(requset, '')

def update(request, article_pk):
    return redirect()

def delete(request, article_pk):
    return redirect()
```

이런식으로!!!

4)) 마스터 앱에 `mkdir templates`폴더 만들기 =>  `touch templates/base.html`

5)) ` mkdir -p articles/templates/articles`

6)) `cd articles/templates/articles/` => `touch new.html index.html detail.html edit.html`  => `cd - `하면 마스터앱으로 나온다.

7)) base.html => 틀 만들기(부트스트랩 cdn 등)

8)) 나머지 html에 

```
{% extends 'base.html' %}
{% block content %}
<h1>detail</h1>

{% endblock content %}
```

이거 쓴 다음에 다른 html에도 복붙.

구조잡기 끝

---

1)) views.py => 이거 추가

```
def contact(request):
    return render(request, 'articles/contact.html')
```

2)) contact.html 추가

```
{% extends 'base.html' %}
{% block content %}
<h1>contact</h1>

{% endblock content %}
```

3)) 앱 urls.py

```
 path('contact/', views.contact, name='contact'),
```

4)) views.py => contact 함수에 contact_form = ContactForm()랑 context 추가

 폼은 왜 쓰는가?

 1) Data Validation

 2) HTML easy

 :: html을 사용하기 쉽게 한다.

5)) contact.html => form 태그 만들기 `<form action="#" method="POST"></form>` => 이 사이에 csrf_token 넣기 => 서버 켜보기 (지금은 crud로만 들어가면 에러뜬다. crud/contact/로 들어가기) => html에  `{{ contact_form.as_p }}` 추가 그러면 요소들이 한 줄 씩 띄어서 뜬다. ===> 이게 바로 그 예시

:: data validation 

6)) views.py에서 

```
if request.method == 'GET':
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'articles/contact.html', context)
    elif request.method == 'POST':
        print(request.POST)  # 처리한 데이터를 보겠다. 
        return redirect('contact')  # 그 다음 보내겠다.
```

이렇게 바꾸면, 같은 url path를 갖고 있지만 get, post로 보내느냐에 따라 다른 일을 하게 한다.

7)) contact.html에서 form 태그 action에 {% url 'contact' %} 추가  => 서버 => 내용 적어서 제출해봤더니

```
<QueryDict: {'csrfmiddlewaretoken': ['r2F64E9FaqbjPlR2wmx14uyptELFLnfnBMC0y5FuQLWe0LL1S6xut9cTbgTs9ZIc'], 'name': ['예리'], 'email': ['syl7280@naver.com'], 'age': ['27'], 'content': ['하이하이']}>
```

터미널에 이게 뜨고, 

```
[16/Mar/2021 14:44:27] "POST /crud/contact/ HTTP/1.1" 302 0
[16/Mar/2021 14:44:27] "GET /crud/contact/ HTTP/1.1" 200 908
```

new와 create의 역할을 동시에 하게 된다.

```
def new(request):
    if request.method == 'GET':
        return render(request, '')
    elif request.method == 'POST':
    ...article.save()
        return redirect('detail')  # 이거 대충 쓴것...
```

new 함수를 이렇게 바꿔주고, contact 함수또한 위에 처럼 합쳐주면 create 함수는 필요없게 된다. 
왜 둘이 합치는지에 대해 생각해봐야한다.

아주 깔끔한 코드가 완성됨. 

---

위에 내용을 설명해보자면 

리퀘스트가 get이냐에따라 post냐에 따라...

1))사용자가 /crud/contact/로 접속 => GET/crud/contact/
=> 요청이 contact 함수의 if GET으로 옴 => 그럼 너는 html을 가져가기 위함이구나! => html을 주는 페이지로 감 그래서 html 받아서 입력 => 제출을 누르는 순간!

2)) 사용자가 HTML > form에서 데이터 제출 => POST
=>contact.html 폼 액션의 경로가 /crud/contact => 그럼 POST/crud/contact/ => 그럼 이거도 contact 함수로 와서 넌 get으로 왔니 post로 왔니? => post로 왔음! => 그럼 넌 제출해야지! => contact로 강제 이동 시켜주세요! => 

:exclamation: 여기서 원칙!!! form에서 버튼 누른거 말고는 무조건 GET! redirect도 get일수밖에 없다.

3)) view 함수에서 contact로 redirect 시킴 => GET/crud/contact/

---

contact.html에 뭐 별로 안 쓴 거 같은데 네임 이런거 다 뜨네??

뷰 함수에 이걸 적고

```
contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'articles/contact.html', context)
```

contact.html에 이걸 적은 결과!!

```
{{ contact_form.as_p}}
```

웹 페이지에 네임 메일 나이 내용이 다 뜨는 것이다!!!

---

이제 데이터 검증을 해야함

1)) views.py contact 함수에서 elif에 추가

```
elif request.method == 'POST':
    contact_form = ContactForm(request.POST)
    return redirect('contact')
```

 어떻게 나오는지 궁금하니 이걸 return위에 넣어보자! `print(contact_form)`

```
[16/Mar/2021 15:16:37] "GET /crud/contact/ HTTP/1.1" 200 908
<tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" value="yeri " maxlength="5" minlength="2" required id="id_name"></td></tr>
<tr><th><label for="id_email">Email:</label></th><td><input type="email" name="email" value="codeyeri7@gmail.com" required id="id_email"></td></tr>
<tr><th><label for="id_age">Age:</label></th><td><input type="number" name="age" value="68" min="3" max="100" required id="id_age"></td></tr>   
<tr><th><label for="id_content">Content:</label></th><td><input type="text" name="content" value="하이하이" required id="id_content"></td></tr> 
[16/Mar/2021 15:16:48] "POST /crud/contact/ HTTP/1.1" 302 0
[16/Mar/2021 15:16:48] "GET /crud/contact/ HTTP/1.1" 200 908
```

이번에는 데이터가 차서 value값이 들어옴.

이 form에 .is_valid()로 유효성검사 가능 / .errors 로 에러 메세지도 친절히 알려줌

아주 똑똑한 애임.

2)) views.py에서 new 함수에 추가

```
elif request.method == 'POST':
    article_form = ArticleForm()
    if article_form.is_valid():
        article.save()
    return redirect('detail')
```

3)) forms.py에서 `class ArticleForm(forms.ModelForm):` 추가 => ArticleForm은 ModelForm이다. model을 연동시킬 수 있음. => 맨 위에 `from .models import Article` 추가 =>

class ArticleForm 안에 추가

```
class Meta:
    model = Article
    fields = '__all__'
```

4)) views.py 맨 위에 ContactForm 뒤에 ArticleForm 추가

5)) new 함수에 이렇게 추가

```
def new(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'articles/new.html', context)
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
			return redirect('detail', article_pk=article.pk)
```

6)) create 함수 제거

7)) 수정

```
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    return render(request, '')
```

왜 뉴는 article_pk이고 얘는 pk이냐? 뉴에 url을 보면 article_pk라는 변수가 있음 url관련된 변수명일뿐. 실제 데이터베이스에서 꺼낼때는 무조건 article.pk

8)) update 함수 제거

```
def edit(request, article_pk):
    if request.method == 'GET':
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'articles/new.html', context)
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('detail', article_pk=article.pk)
```

뉴 함수 복사해와서 edit로 바꿔주기

그리고 `article = get_object_or_404(Article, pk=article_pk)` 추가 -> 제대로 된 것인지 확인해야 해서

9)) `form = ArticleForm(instance=article)` 비어있던 ArticleForm 안에는 instance가 들어와야 한다.

10)) delete는 기존에 만들던 거와 다른게 없으니 오늘은 패스!

---

이제 남은건 html 만드는 것 뿐!

이건 코드 봐라....ㅎ

11)) views.py 다시 넘어가기 => 뉴 함수의 elif 이후를 검증해야 할 듯

서버를 키면 new 페이지에 폼이 제대로 뜬다. 입력해서 제출해보기 => 했더니 디테일 페이지로 잘 넘어감 => elif 부분이 잘 돌아간다고 검증한 것!

12)) form의  action을 비우면 현재 내가 있는 html로 보냄. new.html의 form에서 action을 지우고, method="POST"만 주면 제출버튼을 눌렀을 때 같은 자리로 옴. => 뷰에서 post를 타게됨.
=> method도 지우면 GET으로 요청됨. (뷰에서 get을 타게 됨)

암튼 그래서 new.html와 edit.html의 form action 부분을 지우자. 어차피 같은 위치로 오는 걸.



---

edit과 new의 차이

```
elif request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
```

instance=article 이 부분!!!



new함수에서  post로 올 때 .is_valid로 안 올 떄

```
else:
     return render(request, 'articles/new.html', context)
```

다시 뉴로 가라.



리팩토리부분 음..... 코드 보면서 잘 생각해보기

뉴 함수랑, edit 함수 앞쪽이 리팩토리인듯...ㅎㅎㅎ