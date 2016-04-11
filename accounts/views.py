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

	def create(self, request, user_id):
		# print dir(request)
		# print request.FILES
		post = request.POST
		pictures = request.POST.get('pictures', '')
		content = request.POST.get('content', '')
		print 'pictures ', pictures
		print 'content: ', content
		fortune = Fortune(user_id=user_id, content=content)
		# fortune.save()
		# if pictures:            
		# 	[Picture(fortune=fortune, image=picture) for picture in pictures]

		# queryset = Fortune.objects.filter(user__id=user_id)
		serializer = FortuneSerializer(request.POST)#, many=True)
		return Response(serializer.data)

class FortuneDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fortune.objects.all()
	serializer_class = FortuneSerializer
	lookup_url_kwarg = 'fortune_id'

# ['DATA', 'FILES', 'POST', 'QUERY_PARAMS', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_auth', '_authenticate', '_authenticator', '_content_type', '_data', '_default_negotiator', '_files', '_full_data', '_load_data_and_files', '_load_stream', '_not_authenticated', '_parse', '_request', '_stream', '_user', 'accepted_media_type', 'accepted_renderer', 'auth', 'authenticators', 'content_type', 'csrf_processing_done', 'data', 'negotiator', 'parser_context', 'parsers', 'query_params', 'stream', 'successful_authenticator', 'user', 'version', 'versioning_scheme']