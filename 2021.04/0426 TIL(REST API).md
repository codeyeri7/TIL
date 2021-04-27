# 0426 TIL

## REST API

:rabbit: API(Application Programming Interface)

:carrot: 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

​	--> 어플리케이션과 프로그래밍으로 소통하는 방법

:carrot: 프로그래밍을 활용해서 할 수 있는 어떤 것

:carrot: CLI, GUI는 각각 명령줄과 그래픽(아이콘)을 통해서 특정 기능을 수행하는 것이며 API는 프로그래밍을 통해 그 일을 수행할 수 있음

---

:rabbit: 다양한 interface

CLI : 깃 배쉬

GUI : 바탕화면 아이콘

API : 코드로 작성하는 것(vscode 등에서)

---

:rabbit: Web API

:carrot: 웹 어플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세 (TMDB API 등)

:carrot: 현재 웹 개발은 추가로 직접 모든 것을 개발하지 않고 여러 Open API를 가져와서 활용하는 추세
	ex) 구글, 카카오 지도 API, 우편번호/도로명/지번 검색 API 등

---

:rabbit: REpresentational State Transfer(표현에 대한 상태를 어떻게 정의할 것인가)

:carrot: 웹 설계 상의 장점을 최대한 활용할 수 있는 아키텍처 방법론

:carrot: 네트워크 아키텍쳐 원리의 모음

	1. 자원을 정의
 	2. **자원에 대한 주소를 지정하는 방법**

:carrot: REST 원리를 따르는 시스템 혹은 API를 RESTful API라고 하기도 함

---

:rabbit: REST 구성

:carrot: 자원(URI)

:carrot: 행위(HTTP Method)

:carrot: 표현(Representations)

---

#### URI

:rabbit: Uniform Resource Identifier

:carrot: 통합 자원 식별자

:carrot: 인터넷의 자원을 나타내는 유일한 주소

:carrot: 인터넷에서 자원을 식별하거나 이름을 지정하는 데 사용되는 간단한 문자열

:carrot: 하위개념  --> URL URN

---

#### URL

:rabbit: Uniform Resource Locator

:carrot: 통합 자원 위치

:carrot: 네트워크 상에 자원(리소스)이 어디 있는지(주소)를 알려주기 위한 약속

:carrot: 자원은 HTML 페이지, CSS 문서, 이미지 등이 될 수 있음

:carrot: '웹 주소' 또는 '링크'라고도 불림

---

#### URN

:rabbit: Uniform Resource Name --> (깊이 볼 필요 없음)

:carrot: 통합 자원 이름

:carrot: URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함(독립적 이름)

:carrot: 자원의 이름이 변하지 않는 한 자원의 위치를 이곳저곳 옮겨도 문제없이 동작

:carrot: ex) ISBN (국제표준도서번호) --> ISBN 0-486-27557-4 : 로미오와 줄리엣​

---

:rabbit: URL과 URN 비교 예시

:carrot: "서울특별시 강남구 테헤란로 ㅇㅇㅇㅇㅇ"

​	--> 만약 ㅇㅇㅇㅇㅇ가 새로운 곳으로 이사가게 된다면?

		- 더 이상 '서울특별시 강남구 테헤란로 ㅇㅇㅇㅇㅇ'라는 주소(URL)로 ㅇㅇㅇㅇㅇ를 찾을 수 없음
		- 새로운 주소(URL) '대전광역시 유성구 ㅇㅇㅇㅇㅇ'로 찾아야 함
		- 하지만 ㅇㅇㅇㅇㅇ가 다른 곳으로 가더라도 URN을 통해 ㅇㅇㅇㅇㅇ라는 것을 식별할 수 있다.
		- 즉, ㅇㅇㅇㅇㅇ라는 고유한 이름(URN)은 변함 없음

:carrot: URN은 자원의 ID를 정의하고, URL은 자원을 찾는 방법을 제공 --> 따라서 이 둘은 상호 보완적

---

:rabbit: URI 구조

![](../문서/카카오톡 받은 파일/KakaoTalk_20210428_013813633.jpg)

---

:rabbit: URL과 URI

:carrot: URI는 크게 URL과 URN으로 나눌 수 있지만 URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI를 통칭하는 말로 사용하기도 함

--> :exclamation: 모든 URL은 URI 이지만, 모든 URI가 URL은 아니다!!!!

:star: URL은 path까지!, Query와 fragment는 URI이다.

---

:rabbit: URI 설계 주의사항

:carrot: 밑줄(_)이 아닌 하이픈(-)을 사용 --> URI의 가독성 (띄어쓰기가 된건지 확인이 어렵기 때문에)

:carrot: 소문자 사용 --> 대소문자에 따라 다른 자원으로 인식하게 됨

:carrot: 파일 확장자는 포함시키지 않음​ (ex) naver.com/index.html 과 같은 확장자는 포함 X)

---

#### HTTP

:rabbit: HyperText Transfer Protocol

:carrot: HTML 문서와 같은​ 자원들을 가져올 수 있도록 해주는 프로토콜 (규칙, 약속)

:carrot: 웹에서 이루어지는 모든 데이터 교환의 기초

:carrot: 클라이언트 - 서버 프로토콜

:carrot: 요청(requests) : 클라이언트(브라우저)에 의해 전송되는 메세지

:carrot: 응답(responses​) : 서버에서 응답으로 전송되는 메세지

:carrot: HTTP 특징

​	--> 비연결지향(connectionless) : 서버는 응답 후 접속을 끊음

​	--> 무상태(stateless) : 접속이 끊어지면 클라이언트와 서버 간의 통신이 끝나며 상태를 저장하지 않음 (ex) 로그인과 같은 상태)  - 이를 해결하기위해 쿠키와 세션을 배웠다.

---

:rabbit: HTTP Method

:carrot: 자원에 대한 행위

:carrot: 즉, HTTP는 HTTP Method를 정의하여 주어진 자원에 수행하길 원하는 행동을 나타냄

:carrot: 의미론적으로 행위를 규정하기 때문에 '실제 그 행위 자체가 수행됨'을 보장하진 않음

​	--> GET이 문서 자체를 주는 건 아니다.

:carrot: HTTP verbs 라고도 함​

---

:rabbit: HTTP Method 종류

:carrot: GET : 특정 자원의 표시를 요청하며, 오직 데이터를 받기만 함

:carrot: POST : 서버로 데이터를 전송하며, 서버에 변경사항을 만듦

:carrot: PUT : 요청한 주소의 자원을 수정

:carrot: DELETE : 지정한 자원을 삭제​

우리는 그동안 POST로 CUD를 다 했는데 REST API에서는 PUT이 Update하는 것으로 나뉘어졌다.

---

:rabbit: RESTful한지 안한지?!

:carrot: ​GET/articles/1/read/ --> X  : URI에 불필요한 정보(행위표현)가 포함
--> GET/articles/1/ 이 맞다.

:carrot: GET/articles/1/delete/  --> X : URI는 자원에 대한 행위는 HTTP method로 표현함
--> DELETE/articles/1/ 이 맞다.

---

#### 표현(Representations)

:rabbit: JSON(JavaScript Object Notation)

:carrot: lightweight data-interchange format (가벼운 데이터 포맷)

:carrot: 자바스크립트 객체 문법을 따르며, 구조화된 데이터를 표현하기 위한 문자 기반 데이터 포맷

:carrot: 일반적으로 웹 어플리케이션에서 클라이언트로 데이터를 전송할 때 사용

:exclamation: 자바스크립트 구문에 기반을 두고 있지만 차이점이 있으니 주의

---

:rabbit: JSON 특징

:carrot: 사람이 읽고 쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어 내기 쉬움 (파싱 : 우리가 쓸 수 있는 JSON 객체로 바꾸는 것)

​	--> 파이썬의 dictionary, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value의 구조로 되어 있음

:carrot: 자바스크립트가 아니어도 JSON을 읽고 쓸 수 있는 기능이 다양한 프로그래밍 언어 환경에서 지원됨​

---

:star: REST 핵심 규칙

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 (어떠한)행위는 HTTP Method로 표현한다.

