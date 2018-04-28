from django.conf.urls import url
from .import views
app_name='music'
urlpatterns = [
    #music/
    url(r'^$',views.index, name='index'),
    #music/a.id/
    url(r'^(?P<music_id>[0-9]+)/$',views.detail, name='detail'),
    #music/a.id/favorite
    url(r'^(?P<music_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]