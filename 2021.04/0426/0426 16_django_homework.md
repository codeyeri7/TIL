## Django REST Framework

### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.  T
- HTTP Method는 GET과 POST 두 종류가 있다. F --> GET, POST, PUT, DELETE 4가지가 있다.
- 일반적으로 URI 마지막에 슬래시(/)는 포함하지 않는다.  T
- 'https://www.fifa.com/worldcup/teams/team/43822/create/'는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.  F --> 계층 관계는 잘 표현했지만, 마지막에 슬래시를 포함했기 때문에 RESTful한 URI라고 할 수 없다.

### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

- 200(성공) : 서버가 요청을 제대로 처리했다는 뜻
- 400(잘못된 요청) : 서버가 요청의 구문을 인식하지 못했다.
- 401(권한 없음) : 인증이 필요하다. 서버는 로그인이 필요한 페이지에 대해 이 요청을 제공할 수 있다.
- 403(금지됨) : 서버가 요청을 거부하고 있다.
- 404(찾을 수 없음) : 서버가 요청한 페이지를 찾을 수 없다.
- 500(내부 서버 오류) : 서버에 오류가 발생하여 요청을 수행할 수 없다.

### 3. 아래의 모델을 바탕으로 Serializer를 정의하려 한다.

serializers.py 파일에 StudentSerializer를 작성하시오.

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
```



### 4. Serializers의 의미를 DFR(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

serializers는 queryset과  모델 인스턴스와 같은 복잡한 데이터를 json, xml 또는 다른 콘텐츠 형식으로 쉽게 렌더링 할 수 있게 변환 할 수 있다.

받은 데이터의 유효성을 검사한 후 복잡한 형식으로 다시 변환할 수 있도록 deserialization을 제공한다. REST framework의 serializer는 Django의 Form 및 ModelForm 클래스와 유사하게 동작한다.

