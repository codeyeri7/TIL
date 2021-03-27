# 0326 TIL

브랜치 관리

원격저장소 : 깃랩, 깃허브

로컬저장소 : 지금 내가 사용하는 폴더

이 두 곳에서 동시에 수정해야 하는 경우가 생김 그럴때는?
WEB IDE라는 버튼이 있음. 깃랩 사이트 내에서 수정하고, vscode 안에서 수정하기 => 깃랩 사이트 내에서 커밋이 가능함(update README). 커밋한 후 vscode에서도 git add . / git commit -m 'fix text' 을 한 후(fix text) => 깃랩의 프로젝트 페이지에서 commit을 보면 커밋한 히스토리를 볼 수 있다. => vscode에서 git log --oneline을 쳐보면 update README와 fix text의 히스토리가 달라짐. 커밋의 히스토리가 달라져서 이제 충돌이 일어날 것. => vscode에서 또 수정하고 깃 애드, 깃 커밋(update README) 깃 푸시를 하면 에러 뜸 => errors : failed to push some refs to.. 하면서 git pull하라고 뜸 => git log --one line으로 커밋의 기록을 보며 비교해보자 => 

![image-20210326091303668](C:\Users\codeyeri\AppData\Roaming\Typora\typora-user-images\image-20210326091303668.png)

지금 이렇게 뜸 => 여기서 깃 풀을 하면 원격에 있던 애들을 로컬로 끌고 올 것. 서로 다른 애들을 합칠 것 =>  git pull origin master => 이렇게 하면 원격에만 있던 애가 저 위에 cde랑 a6c 사이에 들어가야 함. 그럼 아니 저 둘이 안에 들어있는 내용이 다른데 어떻게 할 건지 선택하라고 vscode에 뜬다. 난 vscode에서 추가로 저장한 걸 맞다고 할거야(current change) / 난 깃랩에서 적은게 맞다고 할거야(incoming change) 버튼을 vscode에서 누르면 선택이 됨 => 난 새로 수정핡거야 해서 vscode에서 새로 적어서 => 터미널을 보면 master|MERGING이라 뜸 => 이 상태에서 깃 애드 / 깃 커밋을 하면 머징이라는 글자라 사라짐. => git log --oneline을 하면 깃랩에 있던 정보가 로컬에도 들어와져 있는 걸 볼 수 있다. => 그럼 이제 로컬에 있는 애들이 원격에 다시 저장할 것 => git push origin master => 원격에도 똑같이 업로드가 되었다.

---

git reset b2ca1f8 => 리드미의 4,5번 없애고 3번으로 돌아감. git log --oneline을 하면 커밋 기록 자체가 사라진다. 

git revert b2ca1f8 => master|REVERTING이라고 뜸(터미널에) 변경사항 선택하라고 뜸 => 4,5만 지우고 123 남긴 채로 저장할 것임 => git add . / git commit => git log --oneline을 해보면 깃 히스토리는 그대로 진행이 됨. 5번까지 다 있음. 근데 수정한 readme는 123까지. readme가 기억, git log --oneline은 역사라면, 내가 영화를 스포당한 역사는 그대로이지만, 그 기억을 지워버림

근데 이 둘은 그리 자주 사용되지는 않음. 꼭 필요할 때만 사용하기

---

다시 branch로 돌아와서

지금까지 했던거 지우고 다시 해보자!(rm -rf .git)

확인하기.

git init => git add . => git commit => git branch로 브랜치 확인해보기. => 깃이 관리하고 있는 브랜치의 목록이 뜸. 지금은 *master라고 뜨면서 마스터라는 브랜치 위에 있다.

새로운 브랜치를 만들어보자. 

git branch <branch name> 예) git branch change => 체인지라는 브랜치를 만들었음 

새로운 브랜치로 이동해보자

git switch <branch name> => git switch change => 그럼 뒤에 master가 붙었던 게 change로 바뀜.(참고로 이 switch는 2.3 이후의 버전만 가능. 예전 버전은 checkout이다.)

이 브랜치를 여러개 만들 수 있고, 왔다갔다하며 수정도 가능하다.

다시 master 브랜치로 이동! => git switch master

삭제하기

git branch -d <branch name> => git branch -d change => git branch를 하면 master만 남았다고 뜸.

그동안 많이 사용했던 master가 인권 문제로 인해 main으로 바뀌는 추세이다.(마스터가 주종관계를 나타내기 때문에)

깃 애드 / 깃 커밋을 한 후에 브랜치를 나눠보자! 

git branch yeri 새로 만들기 => git log --oneline을 하면 HEAD -> master, yeri가 뜰 것 => 여기서 HEAD는 내가 지금 보고 있는 데이터라는 뜻. => 이 상황에서 git switch yeri로 하고 git log --oneline을 하면 => HEAD -> yeri, master가 뜬다. switch를 하면 HEAD의 위치를 바꾸는 것이다.

readme 내용 추가하고, 지금 내 브랜치가 yeri인 상태에 add / commit 을 한 후 git log --oneline을 하면 master는 아직 아까 커밋한 상태에 남아있고, HEAD-> yeri는 방금 커밋한 위치에 있다.(한 단계 나아감) => 여기서 브랜치를 마스터로 다시 이동해보자 => git switch master를 하면 방금 작성했던 내용이 사라짐. => 다시 git log --oneline을 찍어보면 HEAD->master가 아까 master가 있던 위치에 붙음. => 다시 브랜치를 yeri로 바꿔보면 아까 사라졌던 내용이 다시 생김.

---

master : 실제 돌아가는 서비스

머지하기.

수정하고 애드, 커밋한 후 깃 스위치 마스터 -> git merge change -> Fast-forward 마스터랑 yeri랑 같은 위치가 되었다. 과거에 있던 마스터를 미래로 오게 했다.(마스터 어차피 바뀐거 없으니까) => 이제 둘이 합쳐져서 yeri의 역할은 끝났다. 그러니 삭제해주자. 

뷰.py 만들기 => 깃 branch feature/login => git switch feature/login => viwes.py에 로그인 기능을 완성했다고 치자 => 애드/커밋'로그인기능완성' => 마스터 이동 git switch master => 리드미 수정해서 변경사항 만듬 => 애드/커밋(필요없는문장제거) => 마스터도 한 단계 앞으로 감. => 이 두가지 브랜치가 서로 다른애들을 수정하고 있는 상황 => git merge feature/login => 머지 됐는데.... git log --oneline --graph =>  합쳐지는 과정을 보여주고 있음 => 로그인완성이랑 문장제거랑 하나로 합쳐지고 merge라는 키워드로 합쳐짐. 이게 master로 되고 지금 HEAD도 master에 있다. 그럼 이제 로그인 완성이 만들어 놓은 기능은 이미 마스터가 들고 있어서 이 브랜치의 할 일이 끝났음. 지워주자 => git branch -d feature/login

머지는 메인 줄기에서 해줘야 한다. 외부 줄기를 메인으로 갖고오는게 머지. 근데 이 둘의 충돌이 일어나지 않았던 이유는 마스터는 리드미를 수정하고, 로그인 브랜치는 뷰.py를 수정했기 때문.

뷰.py에 회원가입 기능 구현 후 애드 / 커밋'회원가입' => git branch feature/signup => git switch feature/signup => 이제 내가 담당한 일 하기. 회원가입 기능 완성! => 애드 / 커밋'회원가입 기능 완성' => 내가 완성했다는 리드미에 남기고 싶어서 남김 => 다시 애드 / 커밋'README 작성' => 근데 여기서 다른 사람이 리드미를 수정하고 있었음! git switch master(현재 다른사람 시점) => 애드 / 커밋'readme.md' => 지금 문제가 되는 상황 : 둘 다 리드미를 수정해버림. 이 상태에서 머지 시도 => git merge feature/signup(지금 마스터에 있으니) => 내가 자동으로 하려고 했는데 충돌됏어유... 리드미.md에서 충돌났... => 우리는 충돌된 내용 둘 중 뭐가 맞을 지  선택하기. => 저장한 후 git add / commit 'feature/login branch merge'  => 이제 feature/signup 브랜치의 역할도 끝났으니 삭제

git branch feature/logout => git switch feature/logout => 뷰.py 로그아웃 기능 구현 => 깃 애드 / 커밋'로그아웃 완성' => git push origin feature/logout => 깃랩에 여러개의 브랜치를 볼 수 있게 된다. => 깃랩에서 병합시키기 => git pull origin master => 깃랩에서 병합시킨 부분이 로컬에서도 반영이 되었다.

머지 기능을 사용하고 싶다면 원격이 아닌 로컬에서만 사용하자!

---

a : 코드 작성 전에 내가 사용할 브랜치 만들기 => 브랜치를 내가 만든 걸로 이동 => 내용 작성 후 깃 애드 / 커밋

b : 코드 작성 전에 내가 사용할 브랜치 만들기 => 브랜치 이동 => 내용 작성 후 깃 애드 / 커밋

a와 b는 서로 다른 컴퓨터에서 작성. a : signup 브랜치, b : login 브랜치를 만들어서 작업 중

이제 이를 병합해야 하는데... 얘네를 마스터에서 합쳐야 함. 로컬에서 한다면, 싸인업을 마스터에 병합한 후 b에게 병합했다는 사실을 알려줘야 한다.

a : signup을 master로 병합하기 => git switch master => git merge signup => git push origin master => 싸인업 내용이 마스터에 반영된 상태로 원격저장소에 올라간다. 

이제 b는 a가 바꾼 내용을 원격저장소에서 로컬로 갖고와야 함. => 지금 나는 login 브랜치.. => 이 상태에서 git pull origin master => 이를 하면 브랜치끼리 충돌이 있다고 함. => 둘 다 살리는 것을 선택하고 깃 애드/ 커밋 => git switch master => git pull origin master => git merge login => git push origin master

그럼 이제 a는 또 받아와야 함. git pull origin master => 이래야 전부 싱크가 맞는다. 

---

마스터가 아닌 브랜치끼리의 병합은?

git brach dev를 만들고 옮기고 기능 추가 후 애드 / 커밋 한 후

git branch a => git switch a => a기능 추가하기 => 깃 애드 / 커밋 => git switch dev => git merge a => git switch master => git merge dev

---

월말평가

중요 키워드 

- crud 중 cr이 더 중요하다. 모델폼을 이용한 crud 로직을 짤 수 있어야 한다.

- auth 유저관리. 회원가입, 로그인, 비밀번호 변경, 수정.... 이 중 중요한 건 회원가입을 해야 로그인을 할 수 있고, 로그인을 해야 게시물을 작성할 수 있으니 회원가입과 로그인이 제일 중요!
- 1:N관계까지 다 보기!(어제 본거라 비중은 조금 낮다.)
- import해야 하는 건 명시되어 있다. import 하는 애들이 무슨 역할을 하는지 알아두기