# 0319 TIL

사진이 너무 커요...

posts / detail.html에서 img에서 width를 100%를 주면 화면에 맞게 사진 크기가 조정된다. => 그러나 여기에도 단점이 있다. 작은 사이즈면 확대돼서 사진이 깨지고, 고해상도의 사진도 강제로 작아져서 모두 해상도가 같아지게 된다.

이미지를 규격화하는 방법

구글에 django imagekit을 검색해 pypi사이트로 들어가서 installation을 보라. 우리는 pillow를 이미 다운 받아서 2번으로 가자 2번대로 다운 => 그 밑에 예시 코드를 따라서 진행하자. models.py

```python
image_tumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(100, 50)],
                                format='JPEG',
                                options={'quality': 60})
```

맨 위에 from 2줄도 복붙

그 다음 makemigrations하면 변화사항이 없다고 뜬다. => 일단 서버를 구동해보기

card.html => img src의 post.image.url을 post.image_thumbnail.url로 바꾼다. 근데 이렇게 하니까 난 사진 엑박뜸..교수님은 잘 뜨던데...?ㅠㅠㅠ

(교수님거 참고)이렇게 하면 모두 데이터의 크기가 작아짐. 

models.py에서 아까 image랑 image_tumbnail 주석처리하고

```
image = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
```

이렇게 새로 만들기

그 다음 맨 위에 `from imagekit.models import ProcessedImageField`  넣기

그 다음 makemigrations migrate 해주기(얘는 DB에 영향이 가서 migrate 해준다.)

다시 card.html에서 post.image.url 이걸로 바꾸기

런서버

models.py에서 image에서 upload_to 에 대한 설명
사이트에 사진을 올리면 media라는 파일에 사진이 다 저장되는데 동접자가 많아서 사진이 쌓이면 관리를 해야함. upload_to 속성을 이용해 이미지 경로를 설정. 날짜별로 설정해보자.

`upload_to='images/%Y/%m/%d/'` 이렇게 수정하고 이미지를 업로드해보자! 

그럼 media에 images/2021/03/19 이런 폴더가 생겨서 그 안에 사진이 저장된다.

---

create.html와 edit.html이 똑같다.

그래서 form.html을 만들어주자

views.py에서 create와 update에 update.html이라고 되어있는 부분을 form.html로 고치자.

form.html에 if문이 있다. 경로를 파악해 내가 create로 들어왔는지 update로 들어왔는지 파악 가능

form.html의 block content 바로 밑에 {{ request.resolver_match }}를 적어주니 내 정보를 사이트에 띄어줌.

{% if request.resolver_match.url_name =='ㅇㅇㅇㅇ'%}여기서의 name과 urls.py의 create에서의 네임이 동일해야한다.

---

detail, update, delete의 공통점 : pk라는 값이 필요하다.

만약 pk 값을 현재 없는 번호를 준다면(100..)  => 너 지금 나한테 없는 요청을 하고 있어 라고 해야한다. 너가 잘못했어! 라고 해야하는데 지금은 내가 처리를 못하겠어...라는 식으로 말하고 있음.

100을 일단 찾아보고 없으면 404페이지가 나오도록.

`get_object_or_404` 라는 함수를 사용할것이다.

views.py 맨 위에 get_object_or_404 추가

detail함수 => post = get_object_or_404(Post, pk=pk) => Post로 들어가서 맞는 pk 값을 찾아줘!라고 요청하는 것. 이 때 내가 없는 번호를 입력하면 404페이지가 뜬다. 그럼 사용자가 아 내가 잘못했구나를 알 수 있음

---

:exclamation: media resize는 흐름만 기억하고, form.html로 create와 update를 하나로 합치는것과 get_object_or_404은 꼭 기억하자!!

---

git undo(과거로 돌아가는 것)

사실 시간여행은 안하는게 좋다. 근데 가끔 하는 경우가 생김...ㅎ

a.txt와 b.txt만들고

a.txt를 git add 한 후

다시 내리는 걸 `$ git rm --cached a.txt` 이렇게 하면 된다. (add의 반대) 첫번째로 등록한 애를 돌릴때

그 다음 다시  add하고 commit까지 한 후 a.txt를 수정하고 add한 뒤에 git status했더니 `git restore --staged <file>..." to unstage)` 이렇게 하면 다시 unstage된다고 한다. 수정된 데이터를 다시 돌릴때는 restore 

commit 취소하기
commit시 메세지에 오타를 냄 => 이 메세지를 수정해보자(방금 내가 남긴 커밋만 가능) => `git commit --amend` => 여러 색깔로 보이는 코드가 나타남(vim이라고 한다.) => 이걸 통해 수정하자. 조작법 : 빔은 입력모드와 이동모드 2가지로 나뉜다. / i를 누르면 입력모드(끼워넣기라는 글자 나옴) / esc를 누르면 입력모드를 취소 / 입력모드로 하면 내가 아까 적었던 커밋 메세지가 떠서 그걸 수정할 수 있다. / esc눌러서 입력모드 취소 / 저장은 입력모드가 아닌 상태에서 `:wq`(저장하고 나가겠다는 뜻) + enter 하면 저장됨. / 그 뒤에 git log를 치면 수정한대로 뜬다.

빔을 연습할 수 있는 사이트 : openvim 

c.txt와 d.txt를 만들어서 둘 다 문장을 입력 후 git add c.txt만 함. => 어 난 아까 한 커밋에 d 같이 추가해야하는데 커밋을 남겨버렸다. git commit update c,d => 그래서 지금 아직 c만 올라간 상태 => d를 add하기 git add d.txt => git commit --amend => 이제 하나로 뭉쳐진다. => `:wq` 로 나가기 그럼 마지막 커밋 기록에 c랑 d 같이 들어간 게 뜬다.

버전관리하기 => 아까만든 abcd다 지우고, `rm -rf .git` 다 지우고 새로 시작 => README.md 만들기 => 영화보기라는 시나리오를 적으면서 이 하나하나의 스텝을 커밋으로 남겨보자
1)) 작성 => git init => git add . => git commit -m '영화간 도착' => git log => 영화관 도착이라는 커밋이 남겨짐

2)) ㅈ가성 => git add . => git commit -m '영화표 구매' 

3)) 작성 => git add . => git commit -m '팝콘 구매'

4)) 작성 => git add . => git commit -m '웹서핑'

5)) 작성 => git add . => git commit -m '스포당함'

6)) 작성 => git add . => git commit -m '댓글'

7)) 작성 => git add . => git commit -m '영화보고 나옴'

git log --oneline => 지금 우리가 작성했던 코드 흐름이 나온다. 

이 폴더를 복사해서 3가지의 예시를 보여줌(3개 복사) 과거로 돌아가는 시점을 다르게 줄것임. git reset이라는 명령어를 사용.

1))
hard를 열자 => git log --oneline => 메시지 앞에 5121b0c 이런 코드가 뜬다. 각각의 고유한 코드 => 팝콘구매로 돌아갈거임 git reset --hard 86c4d61(팝콘구매코드) => 그럼 팝콘 구매하는 시점으로 옴. => 이제부터 다시 4번 작성할 수 있음. 과거로 완전히 돌아가는게 hard

2))
soft를 열자 => git log --oneline => git reset --soft 86c4d61 => git log --oneline을 하면 커밋의 시점은 과거로 돌아왔지만, => git status 를 해보면 리드미의 수정사항이 전부 staging area에 올라가있는 걸 알 수 있다. 

3)) mixed => git log --oneline => git reset 86c4d61 (mixed가 기본값이라 아무것도 안 적어도 된다.) =>git log --oneline => git status를 하면 수정사항이 모디파이드되었습니다. add해주세요 즉 add 전 단계까지 간 것.

working directory ---- staging area ---- repository

mixed							soft

이런 느낌. 하드는 working directory까지 수정한 것.

---

