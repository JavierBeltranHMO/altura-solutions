from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(max_length=50, default="More details")
    internal_page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkValue


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card, max length 100 chars",
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card, max length 255 chars",
        required=False,
    )
    image = ImageChooserBlock(help_text="Image will be cropped to 400px by 370px")
    link = Link(help_text="Enter a link or select a page")


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(Card())

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Image will be cropped to 786px by 552px")
    image_alignment = blocks.ChoiceBlock(
        choices=(
            ("left", "Left"),
            ("right", "Right"),
        ),
        default="left",
        help_text="Image on left with text on right or viceversa",
    )
    title = blocks.CharBlock(
        max_length=60,
        help_text="Bold title text for this card, max length 60 chars",
    )
    text = blocks.CharBlock(
        max_length=140,
        help_text="Bold title text for this card, max length 140 chars",
        required=False,
    )

    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"