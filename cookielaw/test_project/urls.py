from .test_app.views import HomeView
from django.conf import settings
from django.conf.urls import url
from django.views import static


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    # required since Django 1.7
    url(r'^static', static.serve, {'document_root': settings.STATIC_ROOT}),
]
