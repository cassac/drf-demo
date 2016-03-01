from django.conf.urls import url, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserView.as_view())

urlpatterns = [
	# url(r'^users/', views.UserView.as_view(), name='user-detail'),
    url(r'^users/(?P<user_id>[0-9]*)$', views.UserView.as_view(), name='user-detail'),
    # url(r'^', include(router.urls)),
    # url(r'users/(?P<user_id>\d+)/fortunes/$', views.FortuneAllViewSet.as_view({'get': 'list'}), name='fortune-detail'),
    # url(r'users/(?P<user_id>\d+)/fortunes/(?P<fortune_id>\d+)/$', views.FortuneViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='fortunes'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]