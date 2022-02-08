# api/serializers.py
from rest_framework import serializers
from newsapp.models import News



class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'title', 'by', 'url', 'title', 'time', 'url')