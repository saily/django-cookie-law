from django.template import Context
from django.template import Template
from django.utils.translation import ugettext as _

import pytest
import six


BANNER_TEMPLATE = """\
{% load cookielaw_tags %}
{% cookielaw_banner %}
"""


@pytest.fixture()
def content(client):
    response = client.get('/')
    assert 200 == response.status_code

    if isinstance(response.content, six.binary_type):
        return response.content.decode('utf-8')  # py3 comapt

    return response.content


def test_banner_shows(content):
    assert 'CookielawBanner' in content


def test_banner_contains_correct_text(content):
    assert _('COOKIE_INFO_HEADER') in content
    assert _('COOKIE_INFO_PARA') in content
    assert _('COOKIE_INFO_OK') in content


def test_banner_render_template_renderer_if_no_cookie_present(request):
    request.COOKIES = {}
    context = Context({'request': request})
    content = Template(BANNER_TEMPLATE).render(context)

    assert _('COOKIE_INFO_HEADER') in content
    assert _('COOKIE_INFO_PARA') in content
    assert _('COOKIE_INFO_OK') in content


def test_banner_render_template_renderer_if_cookie_present(request):
    request.COOKIES = {'cookielaw_accepted': '1'}
    context = Context({'request': request})
    content = Template(BANNER_TEMPLATE).render(context)

    assert '' in content
