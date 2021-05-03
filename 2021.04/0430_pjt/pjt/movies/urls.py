from django.urls import path
from . import views

urlpatterns = [
    # 전체 영화 조회 및 생성
    path('', views.movie_list_or_create),
    # 단일 영화 정보
    path('<int:movie_pk>/', views.movie_detail),
    # 리뷰 생성 
    path('<int:movie_pk>/review/', views.create_review),
    # 리뷰 상세 페이지 (조회, 수정, 삭제) --> 이 페이지에 댓글 생성 & 반환
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_detail_or_update_or_delete),
    # 댓글 생성 
    path('<int:movie_pk>/review/<int:review_pk>/comment/', views.create_comment),
    # 댓글 수정/ 삭제 
    path('<int:movie_pk>/review/<int:review_pk>/comment/<int:comment_pk>/', views.update_or_delete_comment),
]
