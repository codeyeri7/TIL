# Gitlab
## 1. What is the Gitlab - Git '분산형 버젼관리' + '원격 저장소' 

- 프로젝트를 만들때마다 생기는 clone https:주소가 원격 저장소 역할을 해줌 
- Issue tracking이 가능하므로 변경사항 추적 및 각자에게 업무 배분 및 파악 관리 
- Github에 비해 보안 및 개별 프로젝트 진행하기에 용이함 

## 2. 용어 정리 
- server => gitlab / local computer => 내 노트북 

## 3. local에서 git에 업로드할때(push) 

1. 자기소개(내 이메일과 내 이름 등록) -> 내가 올렸다는 걸 모두가 알기 위해서  

   git global setup:  
   ``` 
   git config --global user.name "fromecha" 
   git config --global user.email "fromecha@gmail.com" 
   ```

2. local computer에서 업로드하고 싶은 폴더 경로 설정 
    ```
    mkdir testproject cd testproject
    ```

3. 폴더(testproject)를 git의 관리아래로 두겠다 라고 선언
    ``` 
    git init # 
    (원래 master이지만 인종차별 논란으로 인해 main으로 변경...)
    ```

4. 폴더와 깃랩 연동시켜 깃랩의 저장소를 원격 저장소로 추가하는 작업 
	``` git remote add origin https://~~~ 
	git remote add origin https://~~~
	(https는 gitlab에서 만든 파일을 저장하고 싶은 주소)
```
	
5. 폴더 내에서 코드 작성 및 파일 준비 
	``` touch README.md => 설명서 
	touch.gitignore => 올리고 싶지 않은 파일들 
	```

6.  gitlab에 파일 업로드(파일 경로 및 깃랩 저장소 위치 주의할 것!) 
	``` 
	git add . (전체 분장실로 보내기) 
	git commit -m '명령어' (분장 끝내고 stage로 가기) 
	git push -u origin master (stage위에서 사진찍기) 
	```

## 4. gitlab에서 local로 데이터 다운받기

1. Git의 주소 입력 
	``` 
	git clone https://gitlab주소 
    (local computer에 데이터가 없을 때 원격 저장소의 데이터 가져오기) 
   ```
2. 내 local computer 주소로 이동 
	``` 
	cd 
	cd 내 local computer 저장할 주소 
	```
3. Git에다가 내가 다운받았다는 기록 남기기 
	``` 
	git pull  
	(local computer에 데이터는 이미 있고 원격저장소에 기록 남기기)
   ```