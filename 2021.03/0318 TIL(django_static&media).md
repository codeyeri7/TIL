# 0318 TIL(django_static&media)

#### modelform을 이용해 처음부터 끝까지 작성해보자

1)) modles.py부터 작성 => class Reservation(models.Model): => CharField에서 max_length는 필수이다 => 다 적고 추가로

```
def __str__(self):
	pass 일단 이렇게 적어놓고 
```

2)) 서버 돌리면 urls 없다고 에러 => 앱의 urls.py에서 from 두 줄 적고 `app_name='board'` => urlpatterns 적고 => makemigrations => migrate

3)) forms.py => from 두 줄 (django / .models) => `class ReservationsForm(forms.ModelForm):` => 그 안에 `name = forms.CharField(min_length=2)` => `number = forms.IntegerField(min_value = 0, max_value=4)` + 여기서 완전 새로운 걸(ex. oh = forms.CharField()...) 쓰면 쓰는 족족 인풋이 생긴다. 근데 칸은 만들어지는데 모델 Reservation에 없기 때문에 DB로 저장이 불가.

안써도 되는데 이걸 안 쓰면 추가 상세 설정이 불가.

이건 ModelForm이기 때문에 모델 안에 있는 애들만 상세설정이 가능하다. 새로운건 써봤자 저장이 불가하니 넣지 말자.

그 다음 그 안에 이걸 쓰자.

```
class Meta:
    model = Reservation
    fields = '__all__' 
```

여기서 all은 알아서해주세요 라는 뜻.  

+위젯은 사용자 입력 방법을 좀 더 풍부하게 해주는 역할이다.

name 위젯에 클래스를 주고 싶으면 widget=forms.TextInput(attrs={'class': 'my-class'}) 이런식으로 넣어줄 수 있다.

4)) urls.py => path들 적기(pk적을 때 그냥 적었는데... 교수님은  reservation_pk로 적으심 이건 설정하기 나름) pk는 detail, edit, delete에 추가 

5)) views.py => 함수 틀 만들어주기(일단 다 pass로..ㅎ) => 여기서도 detail, edit, delete는 request, reservation_pk로! (아까 urls에서 변수명을 그렇게 지정했기 때문)=> 맨 위에 `from .models import Reservation`추가 

6)) index 함수에 `reservations = Reservation.objects.order_by('-pk')` => `context = {'reservatons': reservations}` => `return render(request, 'board/index.html', context)`

7)) detail 함수에 => `reservation = Reservation.objects.get(pk어쩌구)` 이렇게 쓰면 잘못되었을 때 네 잘못아니고 서버문제임 이렇게 뜨니까 => 위에 shortcuts에 render 뒤에 get_object_or_404 추가 => `reservation = get_object_or_404(Reservation, pk=reservation_pk)` 여기서 pk 변수명을 reservation_pk라고 설정해놔서. 근데 urls에서 애초에 그냥 pk라고 했으면 여기에도 pk=pk라고 해도 상관없음. => `context = {'reservation': reservation}` => `return render(request, 'board/detail.html', context)`

8)) new 함수에 => `if request.method == 'POST':` => 맨 위에 `from .forms import ReservationForm` 추가 => 다시 new 로 와서 `form = ReservationForm(request.POST)` => 그 안에 `if form.is_valid():`로 유효성검사 => `reservation = form.save()` => 맨 위에 redirect 추가 => `return redirect('detail', reservation.pk)` => else:(겟으로 들어온 경우) => `form = ReservationForm()` => `context = {'form': form}` => `return render(request, 'board/new.html', context)` => is_valid()하지 않을 때를 위해서 context랑 return을 내보내기! 유효하지 않을 때 이 context로 흘러서 나가도록! => 근데 아까 else: (GET인 경우)라고 처음에는 썼지만 근데 이렇게 쓰면 안됨.. GET말고 다른애들도 있기 때문... new에는 GET, POST에만 응답하겠다. 다른 요청방식은 BAD REQEUST야! 라고 하고 싶음. 맨 위에 shortcuts 아래줄에 `from django.views.decorators.http import require_GET(겟으로만 받겠다), require_POST(포스트로만 받겠다), require_http_methods(내가 설정하겠다)` 추가하기 이거 시험에 나올 확률 높음...ㅎ 얘네는 함수인데 데코레이터로 쓰는 방법인 것.=> new함수 위줄에 `@require_http_methods(['GET', 'POST'])`

require_GET 과 require_http_methods(['GET'])이랑 같음. 짧게 쓰려고 줄인 것.

9)) index, detail위 줄에 `@require_GET` 적고 => edit위 줄에 `@require_http_methods(['GET', 'POST'])` => delete 위 줄에 `@require_POST`적기 (앞으로는 이 데코레이터 항상 쓸거임!!!!)

10)) index함수에서 `if request.method == 'GET':` 넣고 그 안에 아까 작성한 reservations랑 context 넣기

11)) 아까 urls.py에서 앱 네임을 적어줬으니까 (앱이 2개 이상이 되면 필수) => redirect에서 앞에 앱네임 다 적어줘야 한다. html에서도 url 'detail' 이렇게 적은걸 url 'articles:detail' 라고 바꿔줘야 함. 예전에 했던거도....!!! 앞으로는 앱이 1개라도 다 이렇게 적을 것이다. 그래서 방금 적었던 board에서도 url 경로에 앱네임 다 추가하기!!! 

12)) edit는 new랑 같아서 복붙하고 => def edit 밑에 `reservation = get_object_or_404(Reservation, pk=reservation_pk)` 추가 => `else:`(get일때) `form = ReservationForm(instance=reservation)` => if request.method == 'POST': 밑에 `form = ReservationForm(request.POST, instance=reservation)` 즉, instance  추가

new는 세상에 없던거를 만드는 거니까 그냥 데이터만 넣어서 진행. 그래서 사용자에게 인풋을 요청할 때도 빈 폼을 보냄. 

edit은 기존에 있던 데이터를 수정하고, 사용자한테 요청을 보낼때도 기존 내용을 같이 보내기 때문에 instance가 필수이다.

13)) delete는 `reservation = get_object_or_404(Reservaion, pk=reservation_pk)` =>` reservation.delete()` => `return redirect('board:index')`

14)) index.html => extends => block content => h1 안에 INDEX => ul => for 문 reservation in reservations => li => a태그 url 'board:detail' reservation.pk 옆에 {{ reservation.name }}

15)) detail.html =>  extends => block content => h1 안에 {{ reservation.name }} => p 안에 `{{ reservation.number }}` => `<a태그 url 'board:edit' reservation.pk> Edit</a>` => `form action=url 'board:delete' reservation.pk` 여기는 action필수 => `method="POST"` => `csrf_token` => `input type="submit" value="삭제" onclick="return confirm('ㄹㅇ?')"`

16)) new.html =>  extends => block content => form action은 없음(제자리에서뛰는거) => method="POST" => csrf_token => {{ form.as_p }} => input type="submit" value="제출!"

form.as_p가 다 좋은데 버튼은 안 만들어준다. 그래서 input 타입 submit 만들어야함. 통일성 때문에 p태그 안에 input 태그 녛어주기

17)) edit.html => extends => block content => form action은 없음(제자리에서뛰는거) => method="POST" => csrf_token => {{ form.as_p }} => input type="submit" value="제출!"

form.as_p가 다 좋은데 버튼은 안 만들어준다. 그래서 input 타입 submit 만들어야함. 통일성 때문에 p태그 안에 input 태그 녛어주기

new랑 edit이랑 html 코드가 완전히 똑같다. 굳이 2개 만들어야 할까?

이건 제안임. 이런 방법도 있다는 것

form.html을 만들어서 아까 적은 내용 복붙. => views.py에서 return할 때 'board/form.html'로 하면 중복을 줄일 수 있다. 

:exclamation: 앞으로 이 코드는 고정이다!!!!!!!!!!!!!!!!!

---

#### static

:bear: static files(정적 파일)

- 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어, 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 즉, 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 응답하면 되는 파일
- 기본 static 경로
  - app_name/static/

```html
{% load static %}
<img src="{% static 'articles/sample.png' %}" alt="sample">
```

:bear: Static Files in settings.py

:honey_pot: STATIC_ROOT

- collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로
- collectstatic : 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업

:honey_pot: STATIC_URL

- STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL

:honey_pot: STATICFILES_DIRS

- app내의 static 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 정의

:bear: media files(미디어 파일)

- 사용자가 웹에서 업로드하는 정적 파일
  - image, pdf, video 등

:bear: Media Files in settings.py

:honey_pot: MEDIA_ROOT

- 사용자가 업로드 한 파일을 보관할 디렉토리의 절대 경로
- 실제 해당 파일의 업로드가 끝나면 어디에 파일이 저장되게 할 지 하는 경로

:honey_pot: MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
- 업로드 된 파일의 주소(URL)를 만들어주는 역할

:honey_pot: MEDIA_URL 및 STATIC_URL은 서로 다른 값을 가져야 함

:bear: 미디어 파일 제공 설정(개발 단계)

- 개발 단계에서는 django.views.static.serve() view를 사용하여 MEDIA_ROOT에서 사용자가 업로드 한 미디어 파일을 제공해야 함

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

새롭게 프로젝트 만들어서 다 설정하기

그 다음에...

index.html에 사진을 넣으려고 img src에 사진 주소를 적었고, 그 다음은 사진을 저장해서 직접 경로를 적어줬더니 => alt+b를 이용해 html을 열었을때는 사진이 2장 다 보였는데 서버로 여니까 위에 하나만 보인다. 그 이유는???

요청 => server => 응답 html  이렇게 받아야 하는데

경로를 적어줬지만, 사용자 입장에서는 요청에 대한 응답 HTML만 받은 것. urls 없이..

그럼 프로젝트 urls.py에 `path('static/<filename>'/, => 어디선가 filename을 찾아라)` 이런 느낌으로 적어줘야 하는데 장고에서 알아서 해줌

settings.py 맨 밑에 static_url이 이 역할을 해줌
STATICFILES_DIRS = [BASE_DIR / 'static']  => 근데 이거 말고 uploader / static / uploader 폴더를 만들고 사진을 uploader로 옮긴다.

index.html에 `<img src="/static/uploader/어서오고.png" alt="come-on">` 이렇게 적으면 서버에서도 사진이 다 보인다.(이건 하드코딩) => `<img src="{% static 'uploader/어서오고.png' %}" alt="come-on">` 이렇게 해주자!

그리고 스태틱 쓸 때 html파일에서 extends 밑에 `{% load static %}`을 꼭 넣어줘야 한다! import 역할

---

static/uploader 안에 css 폴더 만들어주고 그 안에 main.css 만들어 넣고 => images 폴더 만들고 그 안에 사진 넣기

index.html도 사진 위치 수정하기(사이에 images 넣기)

```
<img src="{% static 'uploader/images/어서오고.png' %}" alt="come-on">
```



---

css조정하기 

```
img {
  width: 400px;
  height: 400px;
}
```

main.css에 위와 같이 적은후 => base.html에 block head 를 넣고 => index.html에서 block head에 `<link rel="stylesheet" href="{% static 'uploader/css/main.css' %}">` 적기

이렇게 css 조정을 일일히 하는게 귀찮다! -> base.html 만들어주듯 css도 만들기! => 최상단에 static / css 폴더 만들고 그 안에 base.css 설정해주기(지금은 안하지만 하고 싶으면 이렇게 하면 된다!)

---

upload하는 기능 추가하기

models.py에

```
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

여기서 우리가 ImageField를 사용해서 필수로 `$pip install pillow` 해서 깔아줘야 한다. => `pip freeze > requirements.txt`  해주기.

makemigrations uploader => migrate uploader해주고 db.sqlite3 열어서 sqlite explorer에서 확인해보니 title과 image는 같은 varchar였다. 즉 둘 다 텍스트라는것...! 

---

forms.py => 위에 from 두 줄 쓰고 => class ArticleForm 적고 그 밑에 class Meta: 적기

---

views.py => 이거 추가

```
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from .forms import ArticleForm
```

뉴 함수 적어주기

```
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('uploader:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'uploader/forms.html', context)
```

index에도 @ 추가

---

forms.html 적고, 

```
{% extends 'base.html' %}

{% block content %}
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>


{% endblock content %}
```

urls에 new 추가하기 `path('new/', views.new, name='new'),`

forms.html에 form method 뒤에 ` enctype="multipart/form-data"` 이걸 적어야 파일이 전송된다.

views.py 에  뉴함수에서 if post에서 request.POST 뒤에 `request.FILES` 추가해주기. 그래야 Files을 업로드할 수 있음

---

settings.py에 맨 밑에 `MEDIA_ROOT = BASE_DIR / 'media'` 추가 => 앞으로 미디어는 저기에 저장할거다

스태틱은 개발자들이 사용하는 것. 업로드되는 파일은 전부 랜덤(개발자가 예상 못함. 사용자가 올리니까). 반대로 해더 이미지, 아이콘 이런거는 내가 원해서 집어넣는것. 이게 스태틱이다.

---

프로젝트 urls.py로 가서 

```
from django.conf.urls.static import static
from django.conf import settings
```

추가하고 맨 밑에 urlpatterns 대괄호 뒤에 `\+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` 적기

이 static(웅앵웅)이 함수 자체라 이걸 프린트해보면 [] 리스트로 나온다. 즉 리스트+리스트인 셈.

저 위에 from 2개랑 이걸 안 적으면 사용자 미디어 serving이 안된다. 

---

views.py에 detail 함수 만들기

```
@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'uploader/detail.html', context)
```

---

detail.html에 내용 추가

```
{% extends 'base.html' %}

{% block content %}
<h1>{{ article.title }}</h1>
<p>{{ article.content }}</p>
<img src="{{ article.image.url }}" alt="{{ article.image }}">

{% endblock content %}
```

urls.py에 path detail 추가

---

detail.html에

```
{% if article.image %}

  <img src="{{ article.image.url }}" alt="{{ article.image }}">

{% endif %}
```

이렇게 if로 감싸주면 사진을 안 올려도 에러가 안뜬다. 이렇게 하면 사진을 올릴때만 이미지가 나오도록 하는 것.

if 절 없으면 오류가 뜨게되고 넣으면 안뜨는데 그때 title이랑 content를 난 이미지따윈 안떠 라고 하는것.

---

`$ pip install pilkit django-imagekit` 설치하기

models.py에

```
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
```

```
image = ProcessedImageField(
		upload_to='article/', #지금은 미디어에 떄려박고 있다면 이렇게 하면 article 폴더에 모일 것
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality':90},
    )
```

이렇게 추가

그 다음에 makemigrations uploader 랑 migrate uploader 하기

이렇게 하고 서버 켜서 사진이랑 첨부했더니 사진이 잘림...ㅎ => 우리가 사진 크기 지정해서 잘린거야!(아까 200, 300이라고 해서) 그럼 비율 바꾸는거도 가능? 가능. 근데 지금 하지는 않겠다.

