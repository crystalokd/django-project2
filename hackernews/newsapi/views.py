
from rest_framework import generics
from newsapp.models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer




class NewsList(generics.ListCreateAPIView):
	queryset = News.objects.all()
	serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,) 
	queryset = News.objects.all()
	serializer_class = PostSerializer
