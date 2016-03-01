from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users/(?P<pk>[0-9]*)$', views.UserView.as_view(), name='user-detail'),
    url(r'^users/(?P<user_id>[0-9]*)/fortunes/$', views.FortuneView.as_view(), name='fortune-list'),
    url(r'^users/(?P<user_id>[0-9]*)/fortunes/(?P<fortune_id>[0-9]*)$', views.FortuneDetailView.as_view(), name='fortune-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]