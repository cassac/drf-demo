from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fortune

class FortuneSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fortune
		fields = ('id', 'content',)

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(many=True, read_only=True)
	fortune_list = serializers.HyperlinkedIdentityField(
        view_name='fortune-list',
        lookup_url_kwarg='user_id'
    )

	class Meta:
		model = User
		fields = ('url', 'fortune_list', 'username', 'email', 'is_staff', 'fortunes')
		extra_kwargs = {'url': {'lookup_url_kwarg': 'user_id'}}