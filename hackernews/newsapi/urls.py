
from django.urls import path
from .views import NewsAPIView, NewsDetail



urlpatterns = [
	path('', NewsList.as_view()),
	path('<int:pk>/',NewsDetail.as_view()),
	path('api-auth/', include('rest_framework.urls')),
]