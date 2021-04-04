# 0325 TIL

:bear: 데이터베이스 종류

1)) RDBMS : sqlite, oracla, postgres, mysql 등이 대표적인 제품군

- 특징 : 스키마(schema)이다. 스키마는 컬럼 구조.

2)) NoSQL : mongoDB, firebase db 등이 대표적인 제품군

:bear: 관계형 데이터베이스 : 관계를 표현하기 위해 2차원의 표(table)를 사용.

:bear: sqlite : 서버가 아닌 파일 단위로 돌아가는 가벼운 데이터베이스. 
근데 원래 데이터베이스는 서버여서 프로그램을 돌려야 한다. sqlite만 저러는 것.

:bear: 스키마 : db의 구조와 제약조건에 관련한 전반적인 명세를 기술한 것. 컬럼 구조.

:bear: sql : rdbms의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
 -> sql을 한 단어로 정의하자면 쿼리(물어봄. 질의) rdb에서만 통함

- ddl : 데이터 정의 언어 - 데이터를 정의하기 위한 언어. 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어	
  - models.py에서 하는 일(table 생성, 수정, 삭제)
- dml : 데이터 조작 언어 - 데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어
  - views.py에서 하는 일
- dcl : 데이터 제어 언어 - 데이터베이스 사용자의 권한 제어를 위해 사용되는 언어이다.
  - 장고가 제어하면서 잘 쓰고 있는데 우리는 모름

다시 복습..

last...! 깃 너무 어려워ㅠ

---

00_create_table

```
-- CREATE TABLE classmates (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   name TEXT NOT NULL,
--   age INT NOT NULL,
--   address TEXT NOT NULL
-- );

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  age INTEGER,
  country VARCHAR(50),
  phone VARCHAR(20),
  balance INTEGER
);
```

---

01_delete_table

```
DROP TABLE classmates;
```

---

02_insert

```
INSERT INTO classmates (name, age, address)
VALUES 
('aaa', 100, '대전시'),
('ㅠㅠㅠ', 123, '구미시'),
('ㅎㅎㅎ', 111, '광주시');
```

---

03_select

```
-- 전체 조회
SELECT * FROM classmates;

-- 컬럼 지정 조회
SELECT name, address FROM classmates;

-- 개수 제한(지정)
SELECT id, name FROM classmates LIMIT 1;

-- OFFSET 뒤 부터, LIMIT 개(LIMIT, OFFSET 순서 중요)
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;
```

---

04_where1

```
-- 검색 조건(address == '대전시')
SELECT id, name FROM classmates
WHERE address='대전시';

-- 나이의 값을 가져오기
SELECT DISTINCT age FROM classmates;
```

---

05_delete

```
-- WHERE 조건을 만족하는 데이터 삭제
DELETE FROM classmates WHERE id=1;
-- Table의 데이터 모두 삭제
-- DELETE FROM classmates;
```

---

06_update

```
UPDATE classmates
SET name='서예리', address='서울', age=100
WHERE id=6;

UPDATE classmates
SET name='홍길동', address='제주'
WHERE id=8;
```

---

07_where2

```
-- users에서 age 30 이상
-- SELECT * FROM users
-- WHERE age >= 30;

-- users에서 age 30 이상인 사람의 이름만
-- SELECT first_name FROM users
-- WHERE age >= 30;

-- users에서 age 30 이상, 성이 김인 사람의 성과 나이만
-- SELECT age, last_name FROM users
-- WHERE age >= 30 and last_name = '김';

-- users에서 age 30 이상이거나 성이 김인 사람의 성과 나이만
-- SELECT age, last_name FROM users
-- WHERE age >= 30 or last_name = '김';
```

---

08_expression

```
-- users 레코드의 개수 COUNT
SELECT COUNT(*) FROM users;

-- 30살 이상의 평균나이
SELECT AVG(age) FROM users
WHERE age >= 30;

-- 30살 이상의 평균잔액
SELECT AVG(balance) FROM users
WHERE age >= 30;

-- users에서 계좌 잔액(balance)이 가장 높은 사람과 액수
SELECT first_name, MAX(balance) FROM users;

-- 평균, 개수, 총합
SELECT AVG(balance), COUNT(*), SUM(balance) FROM users;
```

---

09_where3

```
-- 값의 비교가 아닌 패턴의 비교

-- 20대 찾기
SELECT * FROM users
-- WHERE age >= 20 and age < 30;
WHERE age LIKE '2_';

-- 지역번호 02 찾기
SELECT phone FROM users
WHERE phone LIKE '02-%';

-- 박씨이면서 준으로 끝나는 사람의 이름
SELECT last_name, first_name FROM users
WHERE first_name LIKE '%준' and last_name LIKE '박';

-- 번호 중간 번호가 5114인 사람만
SELECT phone FROM users
WHERE phone LIKE '%-5114-%';
```

---

10_order

```
-- 나이순으로 오름차순 정렬하여 상위 10개
SELECT * FROM users
ORDER BY age ASC LIMIT 10;

-- 나이 + 성 순으로 오름차순 정렬하여 상위 10개
SELECT * FROM users
ORDER BY age, last_name ASC LIMIT 10;
-- ORDER BY age, last_name ASC LIMIT 10; => 나이가 어린 사람들 중에서 ㄱㄴㄷ 정렬
-- ORDER BY last_name, age ASC LIMIT 10; => ㄱㄴㄷ 정렬 기준에서 나이 어린 10명

-- 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개
-- 제일 부자 10명의 성과 이름
SELECT last_name, first_name FROM users
ORDER BY balance DESC LIMIT 10;
```

---

11_groupby

```
-- 각 성씨별로 몇 명이 있을까?
-- SELECT DISTINCT last_name FROM users;  -- 발견한 순서대로

SELECT last_name
FROM users
GROUP by last_name;  -- ㄱㄴㄷ 순서


SELECT last_name, COUNT(*) AS name_count -- AS는 컬럼명을 변경한다.(COUNT(*)을 name_count로)
FROM users
GROUP by last_name;  -- last_name이 같은 사람들만 따로 SELECT 구문 진행
```

---

models.py

```
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    balance = models.IntegerField()

```

jupyter notebook

```
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
```

```
from users.models import Customer
```

## 1. Review

```
Customer.objects.all()
```

```
# 나이 30의 이름만
Customer.objects.filter(age=30).values('first_name')

<QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}, {'first_name': '상현'}, {'first_name': '정훈'}, {'first_name': '서연'}, {'first_name': '정식'}, {'first_name': '영수'}, {'first_name': '예진'}, {'first_name': '은지'}, {'first_name': '준영'}, {'first_name': '숙자'}, {'first_name': '현주'}, {'first_name': '성수'}, {'first_name': '상훈'}, {'first_name': '민재'}, {'first_name': '지아'}, {'first_name': '정순'}, {'first_name': '지원'}, {'first_name': '하은'}, '...(remaining elements truncated)...']>
```

```
print(Customer.objects.filter(age=30).values('first_name').query)

SELECT "users_customer"."first_name" FROM "users_customer" WHERE "users_customer"."age" = 30
```

```
# 나이가 30 이상인 사람의 인원 수 COL __gte, __gt, __lte, __lt 컬럼명에 이렇게 붙여야 한다.
Customer.objects.filter(age__gte=30).count()

414
```

```
print(Customer.objects.filter(age__gte=30).query)

SELECT "users_customer"."id", "users_customer"."first_name", "users_customer"."last_name", "users_customer"."age", "users_customer"."country", "users_customer"."phone", "users_customer"."balance" FROM "users_customer" WHERE "users_customer"."age" >= 30
```

```
# 미성년자의 인원수
Customer.objects.filter(age__lt=20).count()

213
```

```
# 30 이면서 동시에 김씨인 사람 수
Customer.objects.filter(age=30, last_name='김').count()

6
```

```
# 30 이상이면서 동시(AND)에 김씨인 사람 수
Customer.objects.filter(age__gte=30, last_name='김').count()

112
```

```
# 30 이상이거나(OR), 강씨인 사람의 수
Customer.objects.filter(Q(age__gte=30) | Q(last_name='강')).count()

425
```

```
(Customer.objects.filter(last_name='강')| Customer.objects.filter(age__gte=30)).count()

425
```

```
# % => 무엇이든, _ => 반드시 그 자리에
# django orm 에서는 % 만 사용 가능. 그 이상으로 패턴 비교를 하려면, 아예 정규표현식(regex)를 사용한다.
# 02- 로 시작하는 전화번호 개수 (02-%)
Customer.objects.filter(phone__startswith='02-').count()

249
```

```
print(Customer.objects.filter(phone__startswith='02-').query)

SELECT "users_customer"."id", "users_customer"."first_name", "users_customer"."last_name", "users_customer"."age", "users_customer"."country", "users_customer"."phone", "users_customer"."balance" FROM "users_customer" WHERE "users_customer"."phone" LIKE 02-% ESCAPE '\'
```

```
# 강원도민 중 황씨 성을 가진 사람의 이름만
Customer.objects.filter(country='강원도', last_name='황').values('first_name')

<QuerySet [{'first_name': '은정'}, {'first_name': '혜진'}, {'first_name': '경수'}, {'first_name': '준영'}]>
```

```
# 나이가 가장 많은 사람 10명 => 자동으로 ORM이 LIMIT, OFFSET을 처리합니다.
Customer.objects.order_by('-age')[:10]
Customer.objects.order_by('-age')[10:20]

<QuerySet [<Customer: Customer object (219)>, <Customer: Customer object (252)>, <Customer: Customer object (346)>, <Customer: Customer object (356)>, <Customer: Customer object (365)>, <Customer: Customer object (368)>, <Customer: Customer object (399)>, <Customer: Customer object (408)>, <Customer: Customer object (431)>, <Customer: Customer object (446)>]>
```

```
# 가장 가난한 10명
Customer.objects.order_by('balance')[:10].values('balance')

<QuerySet [{'balance': 150}, {'balance': 150}, {'balance': 150}, {'balance': 150}, {'balance': 150}, {'balance': 160}, {'balance': 160}, {'balance': 160}, {'balance': 160}, {'balance': 170}]>
```

```
# 가장 가난한 + 최연장자 10명
Customer.objects.order_by('balance', '-age')[:10].values('balance', 'age')

<QuerySet [{'balance': 150, 'age': 33}, {'balance': 150, 'age': 32}, {'balance': 150, 'age': 32}, {'balance': 150, 'age': 28}, {'balance': 150, 'age': 20}, {'balance': 160, 'age': 36}, {'balance': 160, 'age': 32}, {'balance': 160, 'age': 25}, {'balance': 160, 'age': 23}, {'balance': 170, 'age': 37}]>
```

```
# 성 / 이름 ㄱㄴㄷ 정렬 내림차순 기준 5번째
Customer.objects.order_by('-last_name', '-first_name').values()[4]

{'id': 912,
 'first_name': '준영',
 'last_name': '황',
 'age': 16,
 'country': '강원도',
 'phone': '02-1030-5139',
 'balance': 6500}
```



## 2. Annotate

```
from django.db.models import Count
from django.db.models.functions import Concat
```

```
# Concat은 스트링끼리 더하는 것!
Customer.objects.annotate(full_name=Concat('first_name', 'last_name')).values()[4]

{'id': 5,
 'first_name': '영환',
 'last_name': '차',
 'age': 30,
 'country': '충청북도',
 'phone': '011-2921-4284',
 'balance': 220,
 'full_name': '영환차'}
```

```
Customer.objects.annotate(Count('country')).values()[1]

{'id': 2,
 'first_name': '경희',
 'last_name': '이',
 'age': 36,
 'country': '경상남도',
 'phone': '011-9854-5133',
 'balance': 5900,
 'country__count': 1}
```





