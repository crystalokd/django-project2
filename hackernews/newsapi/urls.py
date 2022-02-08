# api/urls.py
from django.urls import path
from .views import BookAPIView



urlpatterns = [
	path('', NewsAPIView.as_view()),
	path('<int:pk>/',NewsDetail.as_view()),
]