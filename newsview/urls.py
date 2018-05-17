"""newsview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from infoview import views as infoviews

urlpatterns = [
    url(r'^lanview', infoviews.lanview, name='lanview'),
    url(r'^timeview', infoviews.timeview, name='timeview'),
    url(r'^mapview', infoviews.mapview, name='mapview'),
    url(r'^topicview', infoviews.topicview, name='topicview'),
    url(r'^time_data/$',infoviews.time_data,name = 'time_data'),
    url(r'^admin/', admin.site.urls),
]
