from django.views.generic import TemplateView

from .models import Slider
from .models import About
from .models import Service
from .models import Testimonial
from .models import Contact
from .models import Footer



class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # slider section
        slider_list = list(Slider.objects.all())
        context['slider_info'] = slider_list
        #print(list(slider_list))

        # about section
        about_list = list(About.objects.all())
        context['about_list'] = about_list

        # service section
        service_list = list(Service.objects.all())
        context['service_list'] = service_list


        # testimonial section
        testimonial_list = list(Testimonial.objects.all())
        context['testimonial_info'] = testimonial_list

        # contact section
        contact_list = list(Contact.objects.all())
        context['contact_list'] = contact_list

        # footer section
        footer_list = list(Footer.objects.all())
        context['footer_list'] = footer_list

        return context

    # def about_data(self, **kwargs):
    #     about_data= super().about_data(**kwargs)
    #     about_list = list(About.objects.all())
    #     #print(list(slider_list))
    #
    #     about_data['about_info'] = about_list
    #
    #     return about_data


class DetailView(TemplateView):
    template_name = "detail.html"


