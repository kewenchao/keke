# -*- coding: utf-8 -*-
from django.conf.urls import url


from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^user$', views.UserList.as_view()),

    url(r'^$', views.index),



]
