# api/views.py
from rest_framework import generics
from books.models import News
from .serializers import NewsSerializer



class BookAPIView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer.


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,) 
	queryset = Post.objects.all()
	serializer_class = PostSerializer
