from django.test import TestCase
from django.template import Context, Template


class IoniconsTemplateTagTest(TestCase):
    def test_email_icon(self):
        context = Context()
        template_to_render = Template(
            '{% load ionicon %}'
            '{% ionicon name="mail-outline" %}'
        )
        raw_html = "<svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'><title>ionicons-v5-o</title><rect x='48' y='96' width='416' height='320' rx='40' ry='40' style='fill:none;stroke:#000;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px'/><polyline points='112 160 256 272 400 160' style='fill:none;stroke:#000;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px'/></svg>"
        rendered_html = template_to_render.render(context)
        self.assertHTMLEqual(raw_html, rendered_html, "Email icon not rendered as expected")
