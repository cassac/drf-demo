from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="accounts/index.html")),
	url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<user_id>[0-9]*)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^users/(?P<user_id>[0-9]*)/fortunes/$', views.FortuneList.as_view(), name='fortune-list'),
    url(r'^users/(?P<user_id>[0-9]*)/fortunes/(?P<fortune_id>[0-9]*)/$', views.FortuneDetail.as_view(), name='fortune-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^pictures/$', views.PictureList.as_view(), name='picture-list'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}), 
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)