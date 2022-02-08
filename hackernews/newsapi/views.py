# api/views.py
from rest_framework import generics
from newsapp.models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer



class NewsAPIView(generics.ListAPIView):
	queryset = News.objects.all()
	serializer_class = BookSerializer.


class NewsList(generics.ListCreateAPIView):
	queryset = News.objects.all()
	serializer_class = PostSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,) 
	queryset = Post.objects.all()
	serializer_class = PostSerializer
