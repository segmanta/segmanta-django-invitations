from django.apps.config import AppConfig


class SegmantaLoginAppConfig(AppConfig):
    name = 'segmanta_login'
    verbose_name = 'SegmantaLogin'


class SegmantaLoginAppConfigtests(SegmantaLoginAppConfig):
    pass
