from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fortune

class FortuneSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Fortune
		fields = ('id', 'content', 'user')

	# def create(self, validated_data):
	# 	# fortune_data = validated_data.pop('fortune')
	# 	print self
	# 	print validated_data
	# 	return 'hello'

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(many=True)
	# fortunes =  serializers.HyperlinkedRelatedField(
	# 	many=True, 
	# 	read_only=True,
	# 	view_name='fortunes-detail'
	# )

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'fortunes',)

	# def create(self, validated_data):
	# 	fortune_data = validated_data.pop('fortune')
	# 	user = User.objects.create(**validated_data)
	# 	Fortune.objects.create(user=user, **profile_data)
	# 	return user