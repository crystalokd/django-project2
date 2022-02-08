import requests

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="task_save_latest_hackernews_item",
    ignore_result=True
)

def get_news(request):
	url = "https://hacker-news.firebaseio.com/v0/topstories.json"
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	response = response[0, 99] 

	for i in response:
		x = str(i)
		url = "https://hacker-news.firebaseio.com/v0/item/" + x + ".json"
		payload = "{}"
		response = requests.request("GET", url, data=payload)
		response.save()

	return render (request, 'news/news.html', { "all_news": 
    all_news} )


