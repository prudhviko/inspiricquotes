from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404 = 'quotesapp.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quotesapp.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
