from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock

import streams.blocks as blocks

new_table_options = {
    "minSpareRows": 0,
    "startRows": 3,
    "startCols": 3,
    "colHeaders": False,
    "rowHeaders": True,
    "contextMenu": [
        "row_above",
        "row_below",
        "---------",
        "col_left",
        "col_right",
        "---------",
        "remove_row",
        "remove_col",
        "---------",
        "undo",
        "redo",
    ],
    "editor": "text",
    "stretchH": "all",
    "height": 108,
    "renderer": "text",
    "autoColumnSize": False,
}


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    max_count = 1
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