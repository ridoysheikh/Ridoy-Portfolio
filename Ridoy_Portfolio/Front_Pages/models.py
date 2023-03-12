from django.db import models
from django.core.files.storage import default_storage
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class navs(models.Model):
    nv_title=models.TextField(max_length=20,null=True, blank=False)
    nv_logo = models.ImageField(upload_to='logo/front')
    seo_title = models.TextField(max_length=200,null=True, blank=False)
    seo_description = models.TextField(max_length=500,null=True, blank=False)
    seo_keys=models.TextField(max_length=500,null=True, blank=False)


    def __str__(self):
        return self.nv_title
    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.nv_logo.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)

class bg_images(models.Model):
    Portrait="Portrait"
    Landscape="Landscape"
    bg_mode_CHOICES = [
        (Portrait, 'Portrait'),
        (Landscape, 'Landscape'),
    ]
    bg_mode = models.CharField(
        max_length=20,
        choices=bg_mode_CHOICES,
        default=Landscape,
        blank=False,
    )
    bg_image=models.ImageField(upload_to='bg_image/front')
    
    def __str__(self):
        return self.bg_mode
    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.bg_image.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)


class profession(models.Model):
    name=models.TextField(max_length=35,null=False, blank=False)
    def __str__(self):
        return self.name

class social_id(models.Model):
    name=models.TextField(max_length=35,null=False, blank=False)
    links=models.TextField(max_length=200,null=False, blank=False)
    logo_img=models.ImageField(upload_to='social_logo/front')


    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.logo_img.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)

class market(models.Model):
    name=models.TextField(max_length=35,null=False, blank=False)
    links=models.TextField(max_length=200,null=False, blank=False)
    logo_img=models.ImageField(upload_to='market/front')


    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.logo_img.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)

class edu_cat(models.Model):
    name=models.CharField(max_length=35,null=False, blank=False)
    def __str__(self):
        return self.name

class educations(models.Model):
    title=models.CharField(max_length=50,null=False, blank=False)
    institute=models.CharField(max_length=50,null=False, blank=False)
    start_year=models.CharField(max_length=10,null=False, blank=False)
    end_year=models.CharField(max_length=10,null=False, blank=False)
    description=models.CharField(max_length=200,null=False, blank=False)
    catagory=models.ForeignKey(edu_cat, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

class Skill_cat(models.Model):
    name=models.CharField(max_length=35,null=False, blank=False)
    def __str__(self):
        return self.name

class skills(models.Model):
    title=models.CharField(max_length=10,null=False, blank=False)
    proggress=models.IntegerField(default=1,validators=[MaxValueValidator(100),MinValueValidator(1)])
    catagory=models.ForeignKey(Skill_cat, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

class contact_info(models.Model):
    title=models.CharField(max_length=100,null=True, blank=False)
    adresses=models.CharField(max_length=100,null=True, blank=False)
    phone=models.CharField(max_length=15,null=True, blank=False)
    email=models.CharField(max_length=50,null=True, blank=False)
    website=models.CharField(max_length=50,null=True, blank=False)

    def __str__(self):
        return self.title

class smtp(models.Model):
    server=models.CharField(max_length=100,null=True, blank=False)
    port=models.IntegerField(default=1,null=True, blank=False)
    username=models.CharField(max_length=100,null=True, blank=False)
    password=models.CharField(max_length=50,null=True, blank=False)
    receiver_mail=models.CharField(max_length=100,null=True, blank=False)

    def __str__(self):
        return self.username