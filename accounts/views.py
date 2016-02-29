from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .serializers import UserSerializer, FortuneSerializer
from .models import Fortune

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['GET', 'POST'])
	def fortunes(self, request, pk=None):
		user = self.get_object()
		
		if request.method == 'GET':
			context = {'request': request}
			queryset = Fortune.objects.all()
			serializer = FortuneSerializer(queryset, many=True, context=context)
			return Response(serializer.data)

		if request.method == 'POST':
			serializer = FortuneSerializer(data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response({'status': 'fortune created'})
			else:
				print serializer.errors
				return Response({'status': 'fortune not created'})


class FortuneViewSet(viewsets.ModelViewSet):

	serializer_class = FortuneSerializer

	def retrieve(self, request, user_id=None, fortune_id=None):
		queryset = Fortune.objects.all()
		fortune = get_object_or_404(queryset, pk=fortune_id)
		serializer = self.get_serializer(fortune, many=False)
		return Response(serializer.data)	

class FortuneAllViewSet(viewsets.ModelViewSet):
    model = Fortune
    serializer_class = FortuneSerializer

    def get_queryset(self):
        user = self.request.user
        return user.fortunes.all()