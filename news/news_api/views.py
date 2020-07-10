from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import get_object_or_404
from django_cron import CronJobBase, Schedule
# Create your views here.


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return Response({"posts": posts_serializer.data})

    def post(self, request):
        post = request.data.get('post')
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Post '{}' created successfully"
            .format(post_saved.title)})

    def put(self, request, pk):
        saved = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Post '{}' updated successfully"
            .format(post_saved.title)
        })

    def delete(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        title_post = post.title
        post.delete()
        return Response({
            "message": "Post with id '{}' and title '{}' has been deleted."
            .format(pk, title_post)
        }, status=204)


class UpvoteCron(CronJobBase):
    RUN_AT_TIMES = ['23:59']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'news_api.views.UpvoteCron'

    def do(self):
        posts = Post.objects.all()
        for post in posts:
            #post.upvotes = 0
            #post.save()
            print(1)
