from django.conf.urls import url, include
from django.contrib import admin

from moxie.views import HomeTemplateView
from ideas.views import *


urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^ideas/explore/(?P<pk>\d+)/$', IdeaDetailView.as_view(), name="idea-detail"),
    url(r'^ideas/explore/$', IdeaListView.as_view(), name="idea-list"),
    url(r'^ideas/create/$', IdeaCreateView.as_view(), name="idea-create"),

    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view(), name="home"),
]
