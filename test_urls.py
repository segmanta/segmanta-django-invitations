from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^invitations/', include('invitations.urls')),
    url(r'^admin/', admin.site.urls),
]

if 'allauth' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^accounts/', include('allauth.urls'))
    )

    from segmanta_login.views import SegmantaSignupView

    urlpatterns.append(
        url(r'^accounts/signup/(?P<invitation_key>[0-9A-Za-z]+)/$', SegmantaSignupView.as_view(),
            name="account_signup")
    )
