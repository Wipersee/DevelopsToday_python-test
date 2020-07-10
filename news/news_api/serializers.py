from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "content", "creation_date"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = [
                "pk",
                "title", "link",
                "creation_date", "upvotes",
                "author", "comments"]

    def create(self, validated_data):
        comments_data = validated_data.pop("comments")
        post = Post.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post

    def update(self, instance, validated_data):
        comments_data = validated_data.pop("comments")
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.upvotes = validated_data.get('upvotes', instance.upvotes)
        instance.author = validated_data.get('author', instance.author)
        for comment_data in comments_data:
            Comment.objects.create(post=instance, **comment_data)
        instance.save()
        return instance