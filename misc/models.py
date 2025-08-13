from django.db import models

from wagtail.models import Page

class MiscPage(Page):
    class Meta:
        verbose_name="Miscellaneous page"
        verbose_name_plural="Miscellaneous pages"
