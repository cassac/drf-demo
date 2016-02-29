from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Fortune

class FortuneSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		model = Fortune
		fields = ('url', 'content',)


class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(
		many=True, 
		# view_name='fortunes',
		# lookup_url_kwarg='fortune_id',
		)

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'fortunes',)