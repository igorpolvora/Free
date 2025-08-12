from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Exibe o nome do usuário
    post = serializers.PrimaryKeyRelatedField(read_only=True)  # ID do post

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']
        read_only_fields = ['id', 'user', 'post', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Exibe o nome do usuário
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)  # Total de likes
    comments = CommentSerializer(many=True, read_only=True)  # Lista de comentários no post

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'created_at', 'likes_count', 'comments']
        read_only_fields = ['id', 'user', 'created_at', 'likes_count', 'comments']
