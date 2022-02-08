
from rest_framework import serializers
from newsapp.models import News



class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'type', 'by', 'url', 'title', 'time', 'kids', 'score')