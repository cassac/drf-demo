from django.shortcuts import render
from django.contrib.auth.models import User
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
			fortunes = []
			for f in user.fortunes.all():
				fortunes.append({
					"id": f.id,
					"content": f.content
					})
			return Response(
					{"fortunes": fortunes}
				)

		if request.method == 'POST':
			# ex data for post request
			# {
			# 	"content": "win a car"
			# }
			serializer = FortuneSerializer(data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response({'status': 'fortune created'})
			else:
				# print serializer.data
				print serializer.errors
				return Response({'status': 'fortune not created'})


# class FortuneViewSet(viewsets.ModelViewSet):
# 	query = Fortune.objects.all()
# 	serializer_class = FortuneSerializer