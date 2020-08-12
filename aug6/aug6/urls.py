from django.conf.urls import url,include
from django.contrib import admin
from music import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gaana/',include('music.control')),
    url(r'^login/',views.Login.as_view()),
    url(r'^signup/',views.Register.as_view()),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)