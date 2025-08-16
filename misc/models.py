from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock
import wagtail.blocks as wagtail_blocks

import streams.blocks as blocks
from home.models import new_table_options


class MiscPage(Page):

    body = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardsBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("cta", blocks.CallToActionBlock()),
            (
                "testimonial",
                SnippetChooserBlock(
                    target_model="testimonials.Testimonial",
                    template="streams/testimonial_block.html",
                ),
            ),
            (
                "pricing_table",
                blocks.PricingTableBlock(table_options=new_table_options),
            ),
            (
                "richtext",
                wagtail_blocks.RichTextBlock(
                    template="streams/simple_richtext_block.html",
                    features=["bold", "italic", "ol", "ul", "link", "h3"],
                ),
            ),
            (
                "large_image",
                ImageChooserBlock(
                    help_text="Image cropped to 1200px by 780px",
                    template="streams/large_image_block.html",
                ),
            ),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Miscellaneous page"
        verbose_name_plural = "Miscellaneous pages"
