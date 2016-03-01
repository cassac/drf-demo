from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Fortune

class FortuneSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fortune
		fields = ('id', 'content',)

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(
		many=True,
		)
	url = serializers.HyperlinkedIdentityField(
		view_name='user-detail',
		lookup_field='pk'
	)	

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'fortunes',)