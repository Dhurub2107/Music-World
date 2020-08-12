from django.conf.urls import url
from . import views
app_name="music"
urlpatterns=[
    url(r'^$',views.Home.as_view(),name='album'),
    url(r'^(?P<pk>[0-9]+)/',views.Songview.as_view(),name="song"),
    url(r'^album/add/$',views.AddAlbum.as_view(),name="add album"),
    url(r'^album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name="update album"),
    url(r'^album/(?P<pk>[0-9]+)/delete/', views.AlbumDelete.as_view(), name="delete album"),
    url(r'^song/add/$', views.AddSong.as_view(), name="add song"),
    url(r'^song/(?P<pk>[0-9]+)/$',views.Play.as_view(),name="play"),
    url(r'^song/(?P<pk>[0-9]+)/delete/', views.SongDelete.as_view(), name="delete song"),
]