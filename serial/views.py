from django.views.generic import TemplateView


class SerialView(TemplateView):
    template_name = "serial/serial_home.html"
