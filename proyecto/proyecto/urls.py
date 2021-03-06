"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from proyecto import settings
from django.conf.urls.static import static
from core.sitemaps import StaticSitemap, DynamicSitemap
from django.contrib.sitemaps.views import sitemap


# Sitemap

sitemaps = {'static' : StaticSitemap, 'dynamic' : DynamicSitemap}


# Django admin custom titles

admin.site.site_header = "Administración de Almanimal"
admin.site.site_title = "Administración de Almanimal"
admin.site.index_title = "Bienvenido a Administración de Almanimal"


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('administracion/', admin.site.urls),


    # Core app urls
    path('', include('adopcion.urls')),

    # Adopcion app urls
    path('', include('core.urls')),

    # Blog app urls
    path('', include('blog.urls')),

    # Usuarios app
    path('', include('usuario.urls')),

    # Allauth
    path('accounts/', include('allauth.urls')),

    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
