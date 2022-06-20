"""HCI_Lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from BlogPost.views import profile, publication, blocked_users, add_publications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile, name="profiles"),
    path('publications/', publication, name="publications"),
    path('blocked_users/', blocked_users, name="blocked_users"),
    path('add_publications/', add_publications, name="add_publications")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # za da mozhe da gi prikazheme fajlovite
