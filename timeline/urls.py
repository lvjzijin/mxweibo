from django.conf.urls import patterns, include, url
from django.contrib import admin
from account import views as accountviews

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'send/', 'timeline.views.send'),
                       )
