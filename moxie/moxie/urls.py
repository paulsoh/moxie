from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from moxie.views import HomeTemplateView
from ideas.views import *
from user.views import *

from api.ideas.views import *

urlpatterns = [
    url(r'^api/ideas/explore/$', IdeaListAPIView.as_view(), name="api-idea"),

    url(r'^auth/verify/phonenumber/(?P<slug>\w+)/$', UserVerifyPhoneView.as_view(), name="verify-phone-result"),
    url(r'^auth/verify/phonenumber/$', UserVerifyPhoneView.as_view(), name="verify-phone"),
    url(r'^ideas/explore/(?P<pk>\d+)/fund/$', FundIdeaAPIView.as_view(), name="idea-fund"),

    url(r'^profile/(?P<slug>\S+)/admin/$', ProfileDashboardTemplateView.as_view(), name="profile-dashboard"),
    url(r'^profile/(?P<slug>\S+)/modify/$', ProfileUpdateTemplateView.as_view(), name="profile-modify"),
    url(r'^profile/(?P<slug>\S+)/$', ProfileTemplateView.as_view(), name="profile"),

    url(r'^summernote/', include('django_summernote.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^ideas/explore/category/(?P<slug>\S+)/$', CategoryListView.as_view(), name="category"),

    url(r'^ideas/explore/(?P<slug>\S+)/update/$', IdeaUpdateView.as_view(), name="idea-update"),
    url(r'^ideas/explore/(?P<slug>\S+)/admin/$', IdeaAdminTemplateView.as_view(), name="idea-admin"),

    url(r'^ideas/explore/(?P<slug>\S+)/comment/$', CommentIdeaAPIView.as_view(), name="idea-comment"),

    url(r'^ideas/explore/(?P<slug>\S+)/$', IdeaDetailView.as_view(), name="idea-detail"),
    url(r'^ideas/explore/$', IdeaListView.as_view(), name="idea-list"),
    url(r'^ideas/create/$', IdeaCreateView.as_view(), name="idea-create"),

    url(r'^auth/logout/', signout, name="logout"),

    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view(), name="home"),
] + static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
    )
