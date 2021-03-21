# 0317 TIL(django_form&decorators)

:bear: Form

- Form은 django 프로젝트의 주요 유효성 검사 도구들 중 하나, 공격 및 우연한 데이터 손상에 대한 중요한 방어수단

-  django는 Form에 관련된 작업의 아래 세 부분을 처리해 줌
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML forms 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리

:bear: Form class

- django Form 관리 시스템의 핵심
- form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러메세지를 결정
- django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 중요 줌

```python
class ArticleForm(forms.Form):
	title = forms.CharField(max_langth=10)
	content = forms.CharField(widget=forms.Textarea)
```

:bear: ModelForm Class

- model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능
- Meta Class
  - Model의 정보를 작성하는 곳
  - 해당 model에 정의한 field 정보를 Form에 적용하기 위함

```python
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'content',)
```

:bear: Form & ModelForm

:honey_pot: Form

- 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성(cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출)
- model에 연관되지 않은 데이터를 받을 때 사용

:honey_pot: ModelForm

- django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
- 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능

:bear: Widgets

- Django의 HTML input element 표현
- HTML 렌더링을 처리
- 주의사항
  - Form Fields와 혼동되어서는 안됨
  - Form Fields는 input 유효성 검사를 처리
  - Widgets은 웹페이지에서 input element의 단순 raw한 렌더링 처리

:bear: Django의 2가지 HTML input 요소 표현 방법

:honey_pot: Form fields

- input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨

:honey_pot: Widgets

- 웹 페이지의 HTML input 요소 렌더링 및 제출(submitted)된 원시 데이터 추출을 처리
- 하지만 widgets은 반드시 form fields에 할당 됨

---

forms.py에 원래는 

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```

이렇게 작성하는게 맞는데, 교수님이 수업하면서 위젯 사용하느라 이것저것 추가해서 Meta 클래스가 내려감.  저렇게 위젯을 사용하면  Meta 클래스가 맨 밑으로 내려가는게 맞다.

위젯 사용시 구조 확인하기! 

---

views.py에서 create에서 context가 밖에 있을 때

상황에 따른 2가지 모습

1. is_valid에서 내려온 form : 에러메세지를 포함한 form

2. else에서 내려온 form : 빈 form

(여기 다시 듣고 천천히 정리하지)

---

서버를 켜서 index 페이지를 들어갔을 때 주소가 없다고 에러가 뜬다면, 테이블이 없어서 그런것. 그 때는 migrate를 해줘야 한다.



create.html 에서 form.as_p를 사용해 일일히 구조를 조정하기가 어렵다.

이럴 때는 공식문서를 확인! working with forms에서 목차에 rendering fields manually로 가서 보자

form.title / form.content 이런식으로 사용할 수 있다. 

거기에 아래쪽에 새로 만들어보자

```html
<form action="" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <input type="submit">
  </form>
```

---

looping over the form's fields

for 태그를 이용해 출력을 하고 있다.

```html
<form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
      {{ field.errors }}
      {{ field.label_tag }}
      {{ field }}
    {% endfor %}
    <input type="submit">
  </form>
```

이렇게도 사용 가능!

---

부트스트랩의 form을 사용하고 싶다.

forms.py의 title의 attrs의 class(위젯의 어트리뷰트 클래스) 뒤에 form-control 추가 / content도 마찬가지

이렇게만 해놓으면 이미 해놨던 애들 모두 부트스트랩의 폼 모양대로 바뀐다!!!

---

errorlist 확인

아까 for 태그 이용해 출력한 코드를 그대로 복사해서 거기에 field.errors 자리에 공식문서에서 복사한 것을 넣어준다. (li를 div로 바꿈!)

```html
{% if field.errors %}
  <ol>
  {% for error in field.errors %}
    <div><strong>{{ error|escape }}</strong></div>
  {% endfor %}
  </ol>
{% endif %}
```

에러메세지를 부트스트랩의 alerts를 사용

```html
 class="alert alert-warning" role="alert">
```

이거를 div 뒤에 넣어주기

![image-20210317105502934](0317 TIL(django_form&decorators).assets/image-20210317105502934.png)

빈 제목과 내용을 제출하면 이런식으로 에러메세지가 뜬다.

---

:exclamation: 부트스트랩 라이브러리 문법 사용해보기!

django bootstrap 5라고 검색 => [django-bootstrap-v5 · PyPI] 여기로 들어가기

```
pip install django-bootstrap-v5
```

이거 설치하기!

이렇게 설정이 추가되었으니 requirements.txt도 업데이트 해주기!
`pip freeze > requirements.txt`

그 후 settings.py의 installed_app에 bootstrap5 등록해주기!

그 다음 공식문서를 보면 bootstrap5를 load해주라고 함 => 예시태그를 보자 => 업데이트쪽 수정해보자!

update.html => extends 밑에 `{% load bootstrap5 %}` 추가하기 => form.as_p 밑에 이거 추가하기

```html
{% bootstrap_form form %}
{% buttons %}
    <button type="submit" class="btn btn-primary">Submit</button>
{% endbuttons %}
```

![image-20210317110434206](0317 TIL(django_form&decorators).assets/image-20210317110434206.png)

이렇게 부트스트랩이 입혀졌다.

---

아까 검색했을 때 그 밑에 뜨는 페이지로 들어가보자(https://django-bootstrap-v5.readthedocs.io/en/latest/) => 퀵스타트 => {% bootstrap_css %} / {% bootstrap_javascript %} 이거를 부트스트랩 cdn 대신 추가하자! => base.html로 들어가서 대신 넣어주기 => 맨 위에 `{% load bootstrap5 %}` 이걸 꼭 넣어줘야 로드된다!!!!

다양한 사용법들은 문서를 확인하기!

다른것도 적용해보자! => 왼쪽 목차에 template tags and filters => bootstrap_form_errors 바로 위에 {% bootstrap_form form layout='inline' %}를 복사해서 => update.html의 bootstrap_form form 밑에 넣어주기(얘는 주석처리) => inline을 horizontal로 바꾸기 

![image-20210317111151292](0317 TIL(django_form&decorators).assets/image-20210317111151292.png)

horizontal은 라벨이 왼쪽 인풋이 오른쪽으로 배치되는 구조인 듯.

---

버튼도 바꿔보자!

buttons에서 이걸 복사해서 붙여보자

```
{% buttons submit='OK' reset="Cancel" %}{% endbuttons %}
```

기존 버튼 태그 전체 다 주석처리하고 붙여넣기

![image-20210317111442076](0317 TIL(django_form&decorators).assets/image-20210317111442076.png)

그럼 이렇게 ok랑 cancel 버튼이 생기는데 수정하다가 다시 원래대로 돌리고 싶으면 cancel을 눌러서 원래 상태로 돌릴수가 있다.(type = reset의 역할, 그래서 그냥 input에 넣어도 가능) 

---

load 태그 좀 더 살펴보기

django template tag 검색 => Built-in template tags and filters 클릭 => 오른쪽 목차에서 load로 들어가기 => 읽어보면 set를 로드한다고 되어있다. 로드를 해서 새로운 태그와 필터들을 그 템플릿 안에서 사용을 하겠다는 뜻.

---

상속이 좀 부족한 거 같은데... 근데 extends는 두 개의 상속을 못 받는다ㅠㅠ

그래서 사용가능한 것이 include => 템플릿에서 다른 템플릿을 불러올 수 있다.

base.html에 navbar를 추가하고 싶은데 그렇게 하면 너무 길어진다ㅠㅠㅠㅠ 이렇게 길어지면 코드의 유지 보수가 힘들어진다. 그래서 navbar 코드만 따로 템플릿을 만들어준다. => 프로젝트 templates에 nav.html을 만들어 navbar 코드를 옮겨넣기 => base.html의 body안에 {% include 'nav.html' %}을 넣으면 적용 가능하다! => 이렇게되면 유지 보수가 쉬워진다.

navbar뿐 아니라 footer, header 등도 추가할 수 있다.

---

:bear: View decorators

:honey_pot: decorator(데코레이터)

- 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 '연장'하게 해주는 함수
- django는 다양한 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공

:honey_pot: Allowed HTTP methods

- 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
- 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed를 return
- require_http_methods(), require_GET(), require_POST(), require_safe()

```python
from django.views.decorators.http import require_http_methods, require_POST

@require_http_methods(['GET', 'POST'])
def create(request):
	pass
	
@require_POST
def delete(request, pk):
	pass
```

---

django view decorators 검색 후 공식문서 들어가기 => Allowed HTTP methods 읽어보고 사용해보자!

views.py에 위쪽에 `from django.views.decorators.http import require_safe` 붙여넣기. 공식문서를 보면 require_get보다는 require_safe를 사용하기를 권장한다고 해서 safe 사용하기 => 우리는 index 페이지에서 사용할 것이기 때문에 def index위에 `@require_safe` 넣어주기(index페이지는 GET 요청방식만 필요하기 때문에 GET일때만 작동되도록 한다.) => 이렇게 하면 `GET/articles/index`로 들어올때만 제대로 작동하고, 나머지 메서드들인 POST / PUT 이런거로 들어오게 되면 'method not allowed'라는 에러메세지가 뜰 것.

create는 POST와 GET만 받는게 구조적으로 가장 이상적이다. 그래서 아까 decorator를 import 해줬던 부분에 require_http_methods()를 추가하기 => def create 위에 `@require_http_methods(['GET', 'POST'])` 넣기

update에도 넣기 => 이거도 GET과 POST만 받으니까 => `@require_http_methods(['GET', 'POST'])` 추가

detail에도 => GET만 받으니까 =>  `@require_safe` 

delete => delete는 POST일때만 삭제했으니까, require_POST를 위에 추가하고, `@require_POST`를 def delete위에 넣는다. => 이제는 delete 뷰함수에 들어왔다면 POST라는 것을 확인할 수 있기 때문에 if와 post가 아니었을 때의 return은 필요없다.

```
if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
return redirect('articles:detail', article.pk)
```

여기에서

```
article.delete()
return redirect('articles:index')
```

이렇게만 남겨준다.

