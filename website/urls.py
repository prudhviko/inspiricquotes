from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quotesapp.sitemap import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

handler404 = 'quotesapp.views.custom_404'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quotesapp.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
