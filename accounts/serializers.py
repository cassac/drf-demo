from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fortune

class SingleFortuneSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fortune
		fields = ('id', 'content',)
		# extra_kwargs = {
		# 	'url': {'view_name': 'fortune-detail', 'lookup_field': 'user_id'},
		# }	

class FortuneSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fortune
		fields = ('url', 'id', 'content',)
		extra_kwargs = {
			'url': {'view_name': 'fortune-list', 'lookup_field': 'user_id'},
		}		

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(
		many=True,
		)

	class Meta:
		model = User
		fields = ('username', 'email', 'is_staff', 'fortunes',)