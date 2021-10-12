"""laporhoax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from account.views import (
    home_view,
    login_view,
    laporan_view,
    berita_view,
    isi_berita_view,
    update_berita_view,
    delete_berita_view,
    user_view,
    logout_view,
    kategori_view,
    keputusan_view,
    detail_berita,)

urlpatterns = [
    path('', login_view, name='main'),
    path('logout/', logout_view, name='logout-view'),
    path('home/', home_view, name='home'),
    path('laporan/', laporan_view, name='laporan'),
    path('kategori/', kategori_view, name='kategori'),
    path('keputusan/', keputusan_view, name='keputusan'),
    path('berita/', berita_view, name='berita'),
    path('berita/add/', isi_berita_view, name='isi-berita'),
    path('berita/update/<pk>', update_berita_view, name='update-berita'),
    path('berita/delete/<pk>', delete_berita_view, name='delete-berita'),
    path('news/<pk>', detail_berita, name='detail-berita'),
    path('account/', user_view, name='account'),
    path('admin/', admin.site.urls),
    path('auth/', include('account.api.urls')),
    path('api/', include('feed.api.urls')),
    path('api/', include('report.api.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
