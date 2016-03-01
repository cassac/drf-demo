from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, SingleFortuneSerializer, FortuneSerializer

from .models import Fortune

class UserView(APIView):
	def get(self, request, user_id=None):
		context = {'request': request}
		users = User.objects.all()
		serializer = UserSerializer(users, many=True, context=context)
		return Response(serializer.data)

class FortuneView(APIView):
	def get(self, request, user_id):
		context = {'request': request}
		fortunes = Fortune.objects.filter(user__id=user_id)
		serializer = FortuneSerializer(fortunes, many=True, context=context)
		return Response(serializer.data)

class FortuneDetailView(APIView):
	def get(self, request, user_id, fortune_id):
		fortune = Fortune.objects.filter(pk=fortune_id).filter(user__id=user_id)
		serializer = SingleFortuneSerializer(fortune, many=True)
		return Response(serializer.data)