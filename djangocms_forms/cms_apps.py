# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class DjangoCMSFormsApphook(CMSApp):
    name = _('Forms')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['djangocms_forms.urls']


apphook_pool.register(DjangoCMSFormsApphook)
