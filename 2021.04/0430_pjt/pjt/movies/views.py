from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Comment
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer 


# 전체 영화 조회 및 생성
@api_view(['GET', 'POST'])
def movie_list_or_create(request):
    # 전체 영화 목록 조회 
    if request.method == 'GET': 
        movies = Movie.objects.all() 
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 새로운 영화 정보 생성 
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 영화 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 리뷰 생성 
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 상세 페이지 (조회, 수정, 삭제) --> 이 페이지에 댓글 생성 & 반환
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    
    # 리뷰 조회 
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)    

    # 리뷰 수정 
    elif request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)     # movie=movie가 필요했음.
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 리뷰 삭제 
    elif request.method == 'DELETE':
        review.delete() 
        data = {
            'success': True, 
            'message': f'<{review.title}> 리뷰가 삭제되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


# 댓글 생성 
@api_view(['POST'])
def create_comment(request, movie_pk, review_pk): 
    # movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    seriallizer = CommentSerializer(data=request.data)
    if seriallizer.is_valid(raise_exception=True):
        seriallizer.save(review=review)
        return Response(seriallizer.data, status=status.HTTP_201_CREATED)


# 댓글 수정/ 삭제 
@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, movie_pk, review_pk, comment_pk): 
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'success': True,
            'message': '댓글이 삭제되었습니다.',
        }            
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
