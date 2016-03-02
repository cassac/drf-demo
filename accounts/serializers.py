from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fortune

# class SingleFortuneSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Fortune
# 		fields = ('id', 'content',)
# 		# extra_kwargs = {
# 		# 	'url': {'view_name': 'fortune-detail', 'lookup_field': 'user_id'},
# 		# }	

class FortuneSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fortune
		fields = ('id', 'content',)

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'is_staff', 'fortunes')
		# lookup_field = 'user_id'