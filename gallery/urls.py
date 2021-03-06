# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import GalleryListView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', GalleryListView.as_view(), name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
