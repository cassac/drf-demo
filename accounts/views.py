from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, FortuneSerializer

from .models import Fortune

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class FortuneList(generics.ListCreateAPIView):
	queryset = Fortune.objects.all()
	serializer_class = FortuneSerializer

	def list(self, request, user_id):
		queryset = Fortune.objects.filter(user__id=user_id)
		serializer = FortuneSerializer(queryset, many=True)
		return Response(serializer.data)

	def perform_create(self, serializer):
		serializer.save(user_id=self.kwargs['user_id'])