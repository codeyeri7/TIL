from rest_framework import serializers
from .models import Movie, Review, Comment


class MovieListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    poster_path = serializers.CharField(max_length=200)

    class Meta:
        model = Movie
        fields = ('title', 'poster_path')

class CommentSerializer(serializers.ModelSerializer): 
    content = serializers.CharField(max_length=100)

    class Meta: 
        model = Comment 
        fields = ('content', )

class ReviewListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ('title',)


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    overview = serializers.CharField(min_length=1)  # 에러나면 max_length를 추가해야 할지도..
    release_date = serializers.DateField()
    poster_path = serializers.CharField(max_length=200)
    review_set = ReviewListSerializer(many=True, read_only=True)  # read_only=True가 없으니 required가 떴다.

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path', 'review_set')


class ReviewSerializer(serializers.ModelSerializer): 
    movie = serializers.CharField(max_length=100)  # movie_pk? 
    movie_title = serializers.CharField(max_length=100, source='movie.title', read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(min_length=1)  ## max_length
    rank = serializers.IntegerField()
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta: 
        model = Review 
        # fields = ('movie_title', 'title', 'content', 'rank')
        fields = '__all__'
        read_only_fields = ('movie', 'movie_title', 'comment_set')



