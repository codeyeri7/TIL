# 0312 TIL(fair project)

:bear: 프로젝트 새로 파기

1)) 빈 폴더 만든 후 그 폴더 안으로 들어가기

2)) 깃 배쉬에 touch .gitignore README.md

3)) vscode로 들어가서 gitignore 파일에 gitignore.io 사이트에서 키워드(python vscode window mac 등) 검색해서 복사한 다음 내용 붙이기

4)) README.md 에 무슨 내용을 쓸지 같이 상의하기.(원래는 서로 느낀 점 각자 써야함 오늘은 같이 쓰기) : 참여자쓰고 나머지는 알아서

5)) 터미널에 `git init` => `python -m venv venv` =>  `source venv/Scripts/activate` => venv 있을 떄만 => `pip ` => `pip freeze => requirements.txt` => 이렇게 하면 나중에 내 페어가 pip install -r requirements.txt 

6)) django-admin startproject pjt 04 . 일단 여기까지 하고 깃에 푸시

---

:bear: 참가자가 해야할 일

1)) git clont <remote-repo-url>

2)) cd pjt04

3)) python -m venv venv

4)) source venv/Scripts/activate  => venv  뜬 지 확인

5)) pip install -r requirements.txt

---

:bear: 깃으로 페어 프로젝트 관리하기

1)) a : 깃랩에서 뉴프로젝트만듬. pjt04 (private로) => 일반-회원에서 페어를 추가하기(메인테이너로) => 페어가 자기 컴에서 클론하기. git clone 주소 => b : 그 다음 페어가 서버를 켜서 열면 안 열림 - 데이터가 없기 때문. 데이터는 깃으로 전달이 불가

그래서 fixture를 해야한다. 

dumpdata : 지금 내가 저장되어 있는 데이터 상태를 기억하는 것.
loaddata : 데이터를 불러오기

2)) a : python manage.py dumpdata movies.movie(무비스(앱이름)안에 있는 movie라는 모델을 dump뜬다) => 엔터누르면 영화정보가 출력됨. 장고가 무비스의 무비 데이터를 다 뽑아옴.

근데 python manage.py dumpdata --indent 4 movies.movie 이렇게 하면 데이터들을 4칸씩 끊어서 저장해서 읽기 쉽게 나온다.

3)) python manage.py dumpdata  --indent 4 movies.movie > movies.json 을 하면 지금은 없는 movies.json이라는 파일에 movies.movie 데이터를 저장한다는 것.

4)) 이제 json을 보내줘야함. movies에 fixtures 폴더를 만들기. 장고가 알아서 templates 경로를 돌듯이 fixtures 경로도 돌 것. 이 안에 movies.json을 넣고 => 이걸 깃으로 푸시하면 => 그럼 페어가 풀하면 fixtures안에 json파일을 받을 것.

5)) 근데 아직 migrate가 안 되어있어서 서버 열어도 에러 => `python manage.py migrate` 를 해줘야함. => 그럼 이제 서버가 열리는데 데이터가 없어서 아무것도 안뜸(지금 표만 그려진 상태)

6)) 데이터를 불러오기 위해 `python manage.py loaddata` 라는 명령어 사용. fixtures 폴더 안에 movies 폴더를 만들고 그 안에 movies.json을 넣는다.(템플릿이랑 똑같이!) => `python manage.py loaddata movies/movies.json` 라고 터미널에 치면 데이터가 저장된다. => 서버 돌리면 이제 데이터가 웹페이지에 다 뜬다.(a가 만들어놓은 더미데이터를 그대로 활용 가능)

:exclamation: ==> 우리는 templates랑 fixtures를 마스터 앱에 저장해놔서 `python manage.py loaddata fixtures/movies/movies.json`이라고 하니까 됐다!!

:exclamation: makemigrations를 하면 models.py를 migration 언어로 번역해줌. -> migrate는 실제 데이터베이스에 적용을 시키는 것.  migrate를 하면 데이터가 들어가는 표를 만들어 주는 것. -> loaddata는 그 표 형식에 맞춰서 json 파일을 불러와서 저장시켜주는 것.

