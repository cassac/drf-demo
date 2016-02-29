from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'users/(?P<pk>\d+)/fortunes/$', views.FortuneAllViewSet.as_view({'get': 'list'}), name='fortune-detail'),
    url(r'users/(?P<user_id>\d+)/fortunes/(?P<fortune_id>\d+)$', views.FortuneViewSet.as_view({'get': 'retrieve'}), name='fortunes'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]