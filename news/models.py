from django.db import models

class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='slider_image', blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.name, self.image)

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #slider = models.ForeignKey(Slider,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.title, self.description)


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='service_image', blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s" % (self.title, self.description, self.image)


class Testimonial(models.Model):
    owner_name = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to='testimonial_image', blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.image, self.owner_name)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.phone_number, self.email_address, self.subject, self.message)


class Footer(models.Model):
    company_name = models.CharField(max_length=200, blank=True)
    logo = models.FileField(upload_to='footer_image', blank=True)
    address = models.TextField()
    email_address = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.logo, self.address, self.email_address, self.company_name)

