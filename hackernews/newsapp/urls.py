from django.urls import  path
from . import views

from .views import ( 
    NewsListView, 
    NewsDetailView, 
    NewsTypeListView,  
    SearchResultsListView 
)
urlpatterns = [
    path('', NewsListView.as_view(), name='news-home'),
    path('type/<str:name>', NewsTypeListView.as_view(), name='news-type'),
    path('news/<uuid:pk>/', NewsDetailView.as_view(), name = 'news_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'), 

]
