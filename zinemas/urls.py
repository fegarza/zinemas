from django.conf.urls import url, include
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
handler404 = 'cms.views.error404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('cms.urls', namespace='cms')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
