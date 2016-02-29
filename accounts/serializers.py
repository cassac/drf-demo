from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Fortune

class FortuneSerializer(serializers.HyperlinkedRelatedField):

	queryset = Fortune.objects.all()

	class Meta:
		model = Fortune
		fields = ('content',)

	def get_url(self, obj, view_name, request, format):
		url_kwargs = {
			'user_id': obj.user.id,
			'fortune_id': obj.id
		}
		return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(
		many=True, 
		view_name='fortunes',
		lookup_url_kwarg='fortune_id',
		)

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'fortunes',)