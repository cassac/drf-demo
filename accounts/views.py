import os
import datetime
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from .serializers import (UserSerializer, FortuneSerializer, PictureSerializer,
	PictureListSerializer)
from .models import Fortune, Picture

class PictureList(generics.ListCreateAPIView):
	queryset = Picture.objects.all()
	serializer_class = PictureListSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_url_kwarg = 'user_id'

class FortuneList(generics.ListCreateAPIView):
	queryset = Fortune.objects.all()
	serializer_class = FortuneSerializer

	def list(self, request, user_id):
		context={'request': request}
		queryset = Fortune.objects.filter(user__id=user_id)
		serializer = FortuneSerializer(queryset, many=True, context=context)
		return Response(serializer.data)

	def create(self, request, user_id):

		post = request.POST
		pictures = request.POST.get('pictures', '')
		content = request.POST.get('content', '')

		fortune = Fortune(user_id=user_id, content=content)
		fortune.save()

		today = datetime.datetime.today()

		if pictures:
			for picture in pictures:
				image = Image.open(picture)
				image_type = picture.split('.')[-1]
				filename = picture.split('/')[-1]
				dir_structure = '%d/%02d/%02d' % (today.year, today.month, today.day)
				path = os.path.join(dir_structure, filename)
				p = Picture(fortune=fortune)
				p.image = path
				p.save()
				full_path = os.path.join(settings.MEDIA_ROOT, path)
				image.save(full_path, image_type)

		queryset = fortune
		serializer = FortuneSerializer(queryset)
		return Response(serializer.data)

class FortuneDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fortune.objects.all()
	serializer_class = FortuneSerializer
	lookup_url_kwarg = 'fortune_id'