"""pastebin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from metas import views

urlpatterns = [

    url(r'^accounts/', include('django.contrib.auth.urls'), {"template_name": "login.html"}),
    url(r'^register/',views.register,name="register"),
    url(r'^admin/', admin.site.urls),
    url(r'^file/(?P<token>[0-9A-Za-z]*)',views.show,name="file"),
    url(r'^files/',login_required(views.get_all),name="all"),
    url(r'^$',views.store.as_view(),name="index")
]
