"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from website.views import simple


from website.views import index

from website.views import queryhtml
from website.views import generalhtml
from website.views import monthlyhtml
from website.views import treatmenthtml
from website.views import agehtml


urlpatterns = [

		url(r'^rvsa', simple),
        url(r'^mvsf', simple),
        url(r'^distages', simple),
        url(r'^correlation', simple),
        url(r'^prophylaxis', simple),
        url(r'^correlation', simple),
        url(r'^Overall', simple),
        url(r'^remission', simple),
        url(r'^active', simple),
        url(r'^other', simple),

		url(r'^$',index),
        url(r'^about',index),
        url(r'^info',index),
		url(r'^queries',queryhtml),
        url(r'^general',generalhtml),
        url(r'^monthly',monthlyhtml),
        url(r'^treatment',treatmenthtml),
        url(r'^age',agehtml)
]
