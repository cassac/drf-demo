from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, FortuneSerializer, PictureSerializer
from .models import Fortune, Picture

class PictureList(generics.ListCreateAPIView):
	queryset = Picture.objects.all()
	serializer_class = PictureSerializer

	def perform_create(self, serializer):
		serializer.save(fortune_id=1)

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
		queryset = Fortune.objects.filter(user__id=user_id)
		serializer = FortuneSerializer(queryset, many=True)
		return Response(serializer.data)

class FortuneDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fortune.objects.all()
	serializer_class = FortuneSerializer
	lookup_url_kwarg = 'fortune_id'