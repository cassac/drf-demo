from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fortune, Picture

class PictureSerializer(serializers.ModelSerializer):

	class Meta:
		model = Picture
		fields = ('id', 'image')

class FortuneSerializer(serializers.ModelSerializer):
	# pictures = PictureSerializer(many=True)
	pictures = serializers.ImageField(max_length=None, allow_empty_file=False)

	class Meta:
		model = Fortune
		fields = ('id', 'content', 'pictures')

	def create(self, validated_data):
		pictures = validated_data.pop('pictures')
		fortune = Fortune.objects.create(user=self.context['request'].user, **validated_data)
		if pictures:
			p=Picture(fortune=fortune)
			p.image.save(str(pictures), pictures)
		return fortune

class UserSerializer(serializers.HyperlinkedModelSerializer):

	fortunes = FortuneSerializer(many=True, read_only=True)
	fortune_list = serializers.HyperlinkedIdentityField(
        view_name='fortune-list',
        lookup_url_kwarg='user_id'
    )

	class Meta:
		model = User
		fields = ('url', 'fortune_list', 'username', 'email', 'is_staff', 
			'fortunes')
		extra_kwargs = {'url': {'lookup_url_kwarg': 'user_id'}}