# 유튜브동작 vuex

`vue add vuex`

필요없는거 삭제

app.vue 원래 있던 거 복사해오기

나머지 파일들도 일단은 다 붙여넣기

vue로 프로젝트를 할 때 모델링은 무엇인가? --> 먼저 생각을 해야하는 부분은 state와 component 구조이다.

뷰엑스로 하면 component 구조가 전보다 훨씬 간단해진다.

이제는 화면구성에 대한 모델링, state 등에 어떤 내용이 들어갈 지 사전에 생각하는 것 뿐.

 `npm i axios`

인덱스 스토어에서 `import axios from 'axios'`

state는 videos:[], selectedVideo: {}, 이거만 넣으면 된다.

---

mutations은 뭘 써야 겠찌 모르겠다면 일단 SET으로 시작

```
SET_VIDEOS(state, videos) { 
	state.videos = videos}
```

이렇게 해도 되고,

```
SET_VIDEOS: (state, videos) => state.videos = videos
```

이렇게 해도 됨

```
SET_SELECT_VIDEO: (state, video) => state.selectedVideo = video
```

이것도 추가하자.

---

actions에서 필요할 거 같은 것은

비디오를 받아오는 과정이 있었다. fetchVideos.

첫번쨰 인자로는 무조건 context, 두번째로 들어올 거는 this.query이기 때문에 일단 query로 넣어준다.

```
fetchVideos(context, query) {
	여기에는 axios 갖고오는 const URL이랑 API_KEY 복붙
	여기에 searchbar에서 axios.get 이하를 다 복사해서 갖고 온다.
	여기서 q:this.query가 아니라 q:query이다.
	.then(res => res.data.items)
	.catch(err => console.error(err))
}
```

`.then(res => res.data.items)` 이게 비디오 덩어리 5개임.

state 변경은 액션에서 할 수 없어서 mutation 호출하기

this.으로 올라가서 쓰는 건 안된다. commit으로 불러와야 함.

`.then(res => context.commit('SET_VIDEOS', res.data.items)` 이렇게 불러와야 한다.

이게 끝...ㅎ

videolistitem에서 onclick에 대응하는 selectvideo를 추가해주자.

```
selectVideo(context, video) {
	이게 탄생했으면 selectedVideo를 부른다.
	context.commit('SET_SELECTED_VIDEO', video)
}
```

context 중에 commit만 쓸 거 같으니 context 를 {commit}으로 변경

```
selectVideo: ({ commit }, video) => commit('SET_SELECTED_VIDEO', video)
```

위를 이렇게 바꿔줄 수 있다.

---

app.vue 

data, methods 필요 없다.

computed는 index.js에서 getters를 추가해 거기로 넣어주자.

index.js

```
getters: {
	isSelectedVideo: state => !!Object.keys(state.selectedVideo).length
	}
}
```

이렇게 해주면 app.vue에서 computed도 필요없다.

---

searchbar

method 필요없음

서치바에서 사용자가 뭔가를 입력하니 여기서부터 시작!

input에서 class만 남기고 다 지운후 v-model을 넣어준다.

`v-model="query" @keypress.enter=""`

엔터를 누르면 fetchvideo를 하게 만들어야 한다.(axios) 값이 아니라 메서드와 연결을 해야한다.

`import { mapActions } from 'vuex'`

```
methods: {
	...mapActions(['fetchVideos', ])
}
```

이러면 keypress.enter에 fetchVideos(query)를 넣어준다.

template에서 videoList 뒤에 다 지우고, searchbar 뒤에도 지운다.

---

videolist 

methods, props 필요 없음

지금 v-for에서 videos가 우리에게 없다.

`import { mapState } from 'vuex'`

```
computed: {
	...mapState(['videos'])
}
```



---

videolistitem

methods 필요 없음

computed는 일단 보류

얘는 props를 지울 수 없다. 받아와야 하니까

리스트를 클릭했을 때 어떻게 해야 하는가?

selectVideo가 일어나면 된다.

`import { mapActions } from 'vuex'`

```
methods: {
	...mapActions(['selectVideo'])
}
```

`@click="selectVideo(video)"`로 수정하기

---

app.vue 

template에서 videodetail에서 밑으로 내려보내주는거 없음 지우기. :selectedVideo어쩌구 이 부분 지우기.

`import { mapGetters } from 'vuex'`

computed에

```
computed: {
	...mapGetters(['isSelectedVideo'])
}
```

---

detail

props 지우고,

`import { mapState } from 'vuex'`

computed에

`...mapState(['selectedVideo'])` 추가하기

그러면 computed 안에 this.selectedVideo는 무엇을 의미하는 것일까?

---

index.js

getters에

```
videoSummary(state) {
	return {
		src: `https://youtube.com/embeb/....`
		title: _.unescape...(this.이 아니라 다 state.으로 바꾸기!! 위 아래 다!)
		decription: _.unescape...
	}
}
```

위에 import _ from 'lodash' 추가

---

detail

template에 

{{ videoSummary.title }}

{{ video...,.,.}}

---

listitem

mapGetters 추가

computed 밑에

`...mapGetters(['videoSummary'])` 넣기

---

index.js

mutations

```
SET_VIDEOS: (state, videos) => {
	state.videos = videos.map(v => {
		v.snippet.title = _.unescape(v.snippet.title)
		v.snippet.description = _.unescape(v.snippet.description) 
		return v
	})
}
```

getters에 videosummary 필요 없어짐. 이거 해서.

대신` videoSrc: (state) => https:...` 이거만 살려둠

detail에 제목들 수정

{{ selectedVideo.snippet.title}}

{{ selectedVideo.snippet.description }}

---

교수님 코드랑 비교해보기

