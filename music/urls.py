from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/create_account
    url(r'^create_account/$', views.UserFormView.as_view(), name='create_account'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/song/add/
    url(r'song/add/$', views.SongAdd.as_view(), name='song-add'),

    # /music/song/1/
    url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/song/1/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

]
