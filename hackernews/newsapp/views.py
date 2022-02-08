from django.shortcuts import render
import requests
from django.views.generic import (
    ListView,
    DetailView
)

from .models import News, Type

def home(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'newsapp/home.html', context)


class NewsListView(ListView):
    model = News
    template_name = 'newsapp/home.html'  
    context_object_name = 'news'
    ordering = ['-time']
    paginate_by = 5

class NewsTypeListView(ListView):
    model = News
    template_name = 'newsapp/news_type.html'  
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        type = get_object_or_404(Type, name=self.kwargs.get('name'))
        return News.objects.filter(type=type).order_by('-time')


class NewsDetailView(DetailView):
    model = News


class SearchResultsListView(ListView):
	model = News
	context_object_name = 'news_list'
	template_name = 'newsapp/search_results.html'


	def get_queryset(self): 
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)