from django.contrib import admin
from . models import Slider
from . models import About
from . models import Service
from . models import Testimonial
from . models import Contact
from . models import Footer

class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'status', )
    list_filter = ('name', )
    search_fields = ('name', )

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','description',  )
    list_filter = ('title', 'description', )
    search_fields = ('title', 'description', )

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'image', 'status', )
    list_filter = ('title', )
    search_fields = ('title', )

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'image', 'status', )
    list_filter = ('status', )
    search_fields = ('status', )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_address', 'subject', 'message', )
    list_filter = ('name', )
    search_fields = ('name', )

class FooterAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'logo', 'address', 'email_address', )
    list_filter = ('address', )
    search_fields = ('address', )

admin.site.register(Slider, SliderAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Footer, FooterAdmin)