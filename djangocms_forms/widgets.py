# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms import widgets
from django.conf import settings
from django.utils.safestring import mark_safe


class TelephoneInput(widgets.TextInput):
    input_type = 'tel'


class SearchInput(widgets.TextInput):
    input_type = 'search'


class DateInput(widgets.TextInput):
    input_type = 'date'


class TimeInput(widgets.TextInput):
    input_type = 'time'


class ReCaptchaWidget(widgets.Widget):

    def render(self, name, value, attrs=None):
        site_id = settings.DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY
        template = '<div class="g-recaptcha" id="%(widget_id)s" data-sitekey="6LcaDh4UAAAAAAwK60ks64civITF7cFEhwCaqZgA"></div>'
        return mark_safe(template % {'widget_id': 'id_%s' % name})

    def value_from_datadict(self, data, files, name):
        return (data.get('g-recaptcha-response', None), )
