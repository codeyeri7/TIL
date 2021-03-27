# pjt 06
## 참여자 : 조정원, 서예리



## 어려웠던 점

- account 구현이 쉽지 않았다. 

  ```python
  def login(request):
  	...
    next_url = request.GET.get('next')
    return redirect(next_url or 'community:index')
  ```

   `@login_required ` 가 적용되어 있는 함수에서 로그인이 되어있지 않으면 로그인 실행창으로 이동하며 다음으로 이동할 url이 생성된다.

  위의 코드처럼 `next_url`인자로 주소를 받아와서 `redirect`에 넘겨주면, 로그인 완료 후 자동으로 해당 페이지로 돌아가게 된다.

- 부트스트랩 적용이 마음만큼 되지 않았다.

  ```html
      <div class="container">
      {% for comment in comments %}
      <hr>
          <div class-"d-flex justify-content-between">
              <p>{{ comment }}</p>
              <p>{{ comment.user }}</p>
          </div>
      {% endfor %}
      </div>
  ```

  댓글과 댓글 작성자를 양 끝으로 보내려고 `d-flex justify-content-between`를 했지만 되지 않았다. for문 때문이 아닐까 생각하는데 해결할 수 없었다.

- base.html

  부트스트랩 폼을 적용하기 위하여 `{% load bootstrap5 %}` 를 적용한 후, cdn 자리에도 `{% bootstrap5_css %}` 를 넣었지만 불러오지 못했다. 결국 그냥 cdn url을 넣어주었다.

  

## 완성페이지 

- index

![index](README.assets/index.png)

- login

![login](README.assets/login.png)

- signup

![signup](README.assets/signup.png)

- review_detail

![review_detail](README.assets/review_detail.png)

## 느낀 점

사실 지난 번에는 네비게이터하다 잘 모르는 부분은 TIL 적어놓은 거 많이 참고했는데 오늘은 최대한 참고하지 않고 서로 머리를 맞대고 해결해보았다. 그렇게 하니까 더욱 공부가 된 것 같아 너무 좋았다.

사실 더 예쁘게 꾸며보고 싶었는데 시간이 많이 부족했다... 주말에 시간에 여유가 생긴다면 좀 더 꾸며보고 싶다.

그리고 오늘 생각보다 모르는 부분이 너무 많았다.. 정말 더 열심히 해야겠다는 생각이 들었다ㅠㅠㅠㅠㅠ