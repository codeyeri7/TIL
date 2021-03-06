# 0428 TIL

## DOM

:rabbit: 브라우저에서 할 수 있는 일

:carrot: DOM 조작

​	--> 문서(HTML) 조작

:carrot: BOM 조작

​	--> navigator, screen, location, frames, history, XHR

:carrot: JavaScript Core​(ECMAScript)

​	--> Data Structure(Object, Array), Conditional Expression, Iteration

---

:rabbit: DOM

브라우저 명을 조작할 수 있다.

:rabbit: BOM 

브라우저 주소 자체를 조작할 수 있다.

---

:rabbit: DOM 이란

:carrot: HTML, XML 등과 같은 문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스

:carrot: 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델

:carrot: 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급

:carrot: 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

:carrot: 주요객체

​	--> window : DOM을 표현하는 창. 가장 최상위 객체 (작업시 생략 가능)

​	--> document : 페이지 콘텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함

​	--> navigator, location, history, screen

---

:rabbit: DOM - 해석

:carrot: Parsing (파싱)

​	--> 구문 분석, 해석

​	--> 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

---

:rabbit: BOM 이란 (Browser Object Model)

:carrot: 자바스크립트가 브라우저와 소통하기 위한 모델

:carrot: 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수당

​	--> 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지의 일부분을 제어 가능

:carrot: window 객체는 모든 브라우저로부터 지원받으며 브러우저 window 자체를 지칭​

window.print() : 인쇄 창

window.open()  : 새로운 탭

window.confirm() : 메세지 및 확인, 취소 버튼이 있는 대화상자 창

window.document : document도 브라우저 내에 종속되어 있기 때문에  window 전역 객체에 포함

---

:rabbit: DOM 조작 - 개념

:carrot: Document는 문서 한 장(HTML)에 해당하고 이를 조작​

:carrot: DOM 조작 순서 :star:

	1. 선택 (select)
	2. 변경 (manipulation)

---

:rabbit: DOM 관련 객체의 상속 구조

<img src="0428 TIL(JavaScript).assets/KakaoTalk_20210429_005753027.jpg" style="zoom:33%;" />

:carrot: EventTarget

​	--> Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스

:carrot: Node

​	--> 여러 가지 DOM 타입들이 상속하는 인터페이스

:carrot: Element

​	--> Document 안의 모든 객체가 상속하는 가장 범용적인 기반 클래스

​	--> 부모인 Node와 그 부모인 EventTarget의 속성을 상속

:carrot: Document

​	--> 브라우저가 불러온 웹 페이지를 나타냄

​	--> DOM 트리의 진입점(entry point) 역할을 수행

:carrot: HTMLElement

​	--> 모든 종류의 HTML 요소

​	--> 부모인 element의 속성 상속

---

:rabbit: DOM 선택 - 선택 관련 메서드

:carrot: Document.querySelector()  :star:

​	--> 제공한 선택자와 일치하는 element 하나 선택

​	--> 제공한 CSS selector를 만족하는 첫번째 element 객체를 반환 (없다면 null)

:carrot: Document.querySelectorAll() :star:

​	--> 제공한 선택자와 일치하는 여러 element를 선택

​	--> 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음

​	--> 지정된 셀렉터에 일치하는 NodeList를 반환

:carrot: getElementById()

:carrot: getElementByTagName()

:carrot: getElementByClassName()

----> 이 3개는 사용하지 않을 것

:carrot: 우리가 querySelector(), querySelectorAll()을 사용하는 이유

​	--> id, class 그리고 tag 선택자 등을 모두 사용가능하기 때문에 더 구체적이고 유연하게 선택 가능

---

:rabbit: DOM 선택 - 선택 메서드별 반환 타입

:carrot: 단일 element

​	--> getElementById()

​	--> querySelector()

:carrot: HTMLColletion

​	--> getElementsByTagName()

​	--> getElementsByClassName()

:carrot: NodeList

​	--> querySelectorAll()

---

:rabbit: DOM 선택 - HTMLCollection & NodeList

:carrot: 둘 다 배열과 같이 각 항목을 접근하기 위한 인덱스를 제공 (유사 배열)

:carrot: HTMLCollection

​	--> name, id, 인덱스 속성으로 각 항목들에 접근 가능

:carrot: NodeList

​	--> 인덱스 번호로만 각 항목들에 접근 가능

​	--> 단, HTMLCollection과 달리 배열에서 사용하는 for each 함수 및 다양한 메서드 사용가능

:exclamation: 이 둘을 Live Collection이라 한다.

:carrot: 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, querySelectorAll()의 의해 반환되는 NodeList는 Static Collection​

---

:rabbit: DOM 선택 - Collection

:carrot: Live Collection

​	--> 문서가 바뀔 때 실시간으로 업데이트

​	--> DOM의 변경사항을 실시간으로 collection에 반영

​	--> 예시) HTMLCollection, NodeList

:carrot: Static Collection (non-live)

​	--> DOM이 변경되어도 collection 내용에는 영향을 주지 않음

​	--> :star: querySelectorAll()의 반환 NodeList만 static

---

:rabbit: DOM 변경 - 변경 관련 메서드

:carrot: Document.createElement()

​	--> 주어진 태그명을 사용해 HTML 요소를 만들어 반환

:carrot: ParentNode.append()

​	--> 특정 부모 노드의 자식 노드 리스트 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입 (반환 값 없음)

​	--> <b>여러 개</b>의 Node 객체, DOMString을 추가할 수 있음

:carrot: Node.appendChild()

​	--> <b>한 노드</b>를 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 삽입 (Node만 추가 가능)

​	--> 만약 주어진 노드가 이미 문서에 존재하는 다른 노드를 참조한다면 새로운 위치로 이동

:carrot: ChildNode.remove()

​	--> 이를 포함하는 트리로부터 특정 객체를 제거

:carrot: Node.removeChild()

​	--> DOM에서 자식 노드를 제거하고 제거된 노드를 <b>반환</b>

​	--> Node는 인자로 들어가는 자식 노드의 부모 노드

---

:rabbit: DOM 변경 - remove() vs removeChild()

```javascript
// remove()
// id가 'content'인 태그를 제거
let el = document.querySelector('#content')
el.remove()

// removeChild()
// 부모 노드를 알 때 지정된 자식 요소를 제거
let parent = document.querySelector('#parent')
let child = document.querySeletor('#child')
let oldChild = parent.removeChild(child)
```

---

:rabbit: DOM 변경 - 변경 관련 속성 (property)

:carrot: Node.innerText

​	--> 노드와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)

​		(사람이 읽을 수 있는 요소만 남김)

​	--> 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용 된 모습으로 표현

:carrot: Element.innerHTML

​	--> 요소(element) 내에 포함 된 <b>HTML 마크업</b>을 반환

​	--> XSS공격에 취약점이 있으므로 사용시 주의

---

:rabbit: XSS (Cross-site scripting)  (참고)

:carrot: 공격자가 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법

:carrot: 이 코드의 실행은 피해자가 하며 공격자가 엑세스 제어를 우회하고 사용자를 가장할 수 있도록 함 (csrf 공격과 유사)

---

:rabbit: DOM 변경 - 변경 관련 속성 (property)

:carrot: ​Element.setAttribute(name, value)

​	--> 지정된 요소의 값을 설정

​	--> 속성이 이미 존재하면 값을 업데이트, 그렇지 않으면 지정된 이름과 값으로 새 속성 추가

:carrot: Element.getAttribute()

​	--> 해당 요소의 지정된 값(문자열)을 반환

​	--> 인자는 값을 얻고자 하는 속성의 이름

---

:rabbit: DOM 조작 - 정리

1. 선택한다.

   --> querySelector()

   --> querySelectorAll()

2. 변경한다.

   --> innerText

   --> innerHTML

   --> setAttribute()

   --> getAttribute()

   --> element.style.color

   --> createElement()

   --> appendChild() 등등...

   오늘 배운 변경하는 메서드, 프로퍼트 들은 다 알아야 한다.

---

## Event

:rabbit: Event

:carrot: 네트워크 활동 혹은 사용자의 상호작용 같은 사건의 발생을 알리기 위한 객체

:carrot: 이벤트는 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동에 의해 발생할 수도 있고, 특정 메서드를 호출(HTMLElement.click())하여 프로그래밍적으로도 만들어낼 수 있음

:carrot: 이벤트 처리기 (Event-handlers)

​	--> EventTarget.addEventListener()

​	--> 해당 메서드를 통해 다양한 요소에서 이벤트를 붙일 수 있음

​	--> removeEventListener()를 통해 이벤트를 제거 가능

:rabbit: Event 기반 인터페이스

:carrot: AnimationEvent, ClipboardEvent, DragEvent 등

:carrot: 그 중에서도 "UIEvent" :star:

​	--> 간단한 사용자 인터페이스 이벤트

​	--> Event의 상속을 받음

​	--> MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할을 함

:exclamation: Event : ~하면 ~한다. --> 클릭하면 경고창을 띄운다. / 특정 이벤트가 발생하면 할 일을 등록한다.

:rabbit: Event handler

:carrot: EventTarget.addEventListener()

:carrot: 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정

:carrot: 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능

:carrot: target.addEventListener(type, listener[, options])

​	--> type : 반응 할 이벤트 유형 (대소문자 구분 문자열)

​	--> listener : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체. EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

![](0428 TIL(JavaScript).assets/KakaoTalk_20210429_005154987.jpg)

---

### 세미콜론

:rabbit: 세미콜론 (semicolon)

:carrot: 자바스크립트는 세미콜론을 선택적으로 사용 가능

:carrot: 세미콜론이 없을 경우 ASI에 의해 자동으로 세미콜론이 삽입됨

​	--> ASI : 자동 세미콜론 삽입 규칙

:carrot: 본 수업에서는 자바스크립트의 문법 및 개념적 측면에 집중하기 위해 세미콜론을 사용하지 않고 진행

---

### ECMA

:rabbit: ECMA

:carrot: ECMA(ECMA International)

​	--> 정보 통신에 대한 표준을 제정하는 비영리 표준화 기구

:carrot: ECMAScript는 ECMA에서 ECMA-262 규격에 따라 정의한 언어

​	--> ECMA-262 : 범용적인 목적의 프로그래밍 언어에 대한 명세

:carrot: ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세를 말함

​	--> (참고) ECMAScript6의 발표 연도에 따라 ECMAScript2015라고도 불림

---

#### 변수와 식별자

:rabbit: 식별자 정의와 특징

:carrot: 식별자(identifier​)는 변수를 구분할 수 있는 변수명을 말함

:carrot: 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작

:carrot: 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

:carrot: 예약어 사용 불가능

​	--> 예약어 예시 : for, if, case 등

---

:rabbit: 식별자 작성 스타일

:carrot: 카멜 케이스(camelCase, lower-camel-case) : 두번째 단어의 첫글자부터 대문자

​	--> 변수, 객체, 함수에 사용

:carrot: 파스칼 케이스(PascalCase, upper-camel-case) : 모든 글자의 첫번째 글자를 대문자로 작성

​	--> 클래스, 생성자에 사용

:carrot: 대문자 스네이크 케이스(SNAKE_CASE) : 모든 단어 대문자 작성 & 단어 사이에 언더스코어 삽입

​	--> 상수(constants)에 사용 - 상수란? : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 말함 ex) TOKEN

---

:rabbit: 변수 선언 키워드 (let, const)

:carrot: let

​	--> <b>재할당 할 수 있는</b> 변수 선언 시 사용

​	--> 변수 재선언 불가능

​	--> 블록 스코프

:carrot: const

​	--> <b>재할당 할 수 없는</b> 변수 선언 시 사용

​	--> 변수 재선언 불가능

​	--> 블록 스코프

---

:rabbit: 선언, 할당 그리고 초기화 (참고)

:carrot: 선언(Declaration) : 변수를 생성하는 행위 ​또는 시점

:carrot: 할당(Assignment) : 선언된 변수에 값을 저장하는 행위 또는 시점

:carrot: 초기화(Initialization) : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

---

:rabbit: 변수 선언 키워드 (let, const) 예시 (1) - 재할당

:carrot: let (재할당 가능)

```javascript
let number = 10  // 1. 선언 및 초기값 할당
number = 10      // 2. 재할당

console.log(number) // 10
```

:carrot: const (재할당 불가능)

```javascript
const number = 10  // 1. 선언 및 초기값 할당
number = 10		   // 2. 재할당 불가능

=> Uncaught TypeError
   : Assignment to constant variable.
```

:rabbit: 변수 선언 키워드 (let, const) 예시 (2) - 재선언

:carrot: let (재선언 불가능)

```javascript
let number = 10  // 1. 선언 및 초기값 할당
let number = 50  // 2. 재선언 불가능

=> Uncaught SyntaxError
   : Identifier 'number' has already been declared
```

:carrot: const (재선언 불가능)

```javascript
const number = 10  // 1. 선언 및 초기값 할당
const number = 50  // 2. 재선언 불가능

=> Uncaught SyntaxError
   : Identifier 'number' has already been declared
```

---

:rabbit: 변수 선언 키워드 (let, const)

:carrot: 블록 스코프 (block scope)

​	--> if, for, 함수 등의 <b>중괄호 내부</b>를 가리킴

​	--> 블록 스코프를 가지는 변수는 <b>블록 바깥에서 접근 불가능</b> 

:exclamation: 중괄호 안에 있는 애와 밖에 있는 애는 서로 남남이다. 현재 결과값도 다름!

```javascript
let x = 1

if (x === 1) {
	let x = 2
	console.log(x)  // 2
}

console.log(x)  // 1
```

---

:rabbit: 변수 선언 키워드(var)

:carrot: var

- <b>var로 선언한 변수는 재선언 및 재할당 모두 가능</b> (이거 좋은 말이 아님...)
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅*되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프
  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

- 호이스팅* (hoisting)
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환

---

### 정리

- 자바스크립트 변수 선언 시 사용 가능한 키워드는 const와 let 뿐이다. --> F
  - 자바스크립트 변수 사용시 사용 가능한 키워드는 const, let 그리고 var이다.
- const 키워드로 선언한 변수는 재할당이 가능하다. --> F
  - const 키워드로 선언한 변수는 재할당이 불가능하다.
- let 키워드로 선언한 변수는 재할당이 가능하다. --> T

| 키워드 | 재선언 | 재할당 | 스코프      | 비고         |
| ------ | ------ | ------ | ----------- | ------------ |
| let    | X      | O      | 블록 스코프 | ES6부터 도입 |
| const  | X      | X      | 블록 스코프 | ES6부터 도입 |
| var    | O      | O      | 함수 스코프 | 사용 X       |

