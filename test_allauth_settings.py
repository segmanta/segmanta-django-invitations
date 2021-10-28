from test_settings import *

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'invitations',
    'tests',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'

INSTALLED_APPS = INSTALLED_APPS + ('segmanta_login.apps.SegmantaLoginAppConfig', )
OPEN_REGISTRATION = True
