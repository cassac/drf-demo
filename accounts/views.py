from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .serializers import UserSerializer, FortuneSerializer
from .models import Fortune

class UserView(APIView):

	def get(self, request, user_id=None):
		print 'gettings, ', user_id
		context = {'request': request}
		users = User.objects.all()
		print users
		serializer = UserSerializer(users, many=True, context=context)
		return Response(serializer.data)
		# return Response({'status': 'fortune not created'})
	# queryset = User.objects.all()
	# serializer_class = UserSerializer

	# @detail_route(methods=['GET', 'POST'])
	# def fortunes(self, request, pk=None):
	# 	user = self.get_object()
		
	# 	if request.method == 'GET':
	# 		context = {'request': request}
	# 		queryset = Fortune.objects.all()
	# 		serializer = FortuneSerializer(queryset, many=True, context=context)
	# 		return Response(serializer.data)

	# 	if request.method == 'POST':
	# 		serializer = FortuneSerializer(data=request.data, partial=True)
	# 		if serializer.is_valid():
	# 			serializer.save()
	# 			return Response({'status': 'fortune created'})
	# 		else:
	# 			print serializer.errors
	# 			return Response({'status': 'fortune not created'})


class FortuneViewSet(viewsets.ModelViewSet):

	serializer_class = FortuneSerializer

	def retrieve(self, request, user_id=None, fortune_id=None):
		print 'RETRIEVING'
		queryset = Fortune.objects.filter(user=user_id).all()
		fortune = get_object_or_404(queryset, pk=fortune_id)
		serializer = FortuneSerializer(fortune, many=False)
		return Response(serializer.data)	

	def update(self, request, user_id=None, fortune_id=None):
		print 'UPDATE'
		return Response({'status': 'fortune not created'})

class FortuneAllViewSet(viewsets.ModelViewSet):
    model = Fortune
    serializer_class = FortuneSerializer

    def get_queryset(self):
    	print 'getting'
        user = self.request.user
        return user.fortunes.all()