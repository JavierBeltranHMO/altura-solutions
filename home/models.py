from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField

from streams.blocks import TitleBlock, CardsBlock


class HomePage(Page):
    lead_text = models.CharField(
        max_length=140, blank=True, help_text="Subheading text under banner title"
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select optional page to link to",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50, default="Read More", blank=False, help_text="Button text"
    )
    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Banner backgroundimage",
        on_delete=models.SET_NULL,
    )

    body = StreamField(
        [
            ("title", TitleBlock()),
            ("cards",CardsBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        FieldPanel("banner_background_image"),
        FieldPanel("body"),
    ]
