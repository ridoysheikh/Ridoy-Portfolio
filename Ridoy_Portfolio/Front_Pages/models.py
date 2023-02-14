from django.db import models
from django.core.files.storage import default_storage

# Create your models here.
class navs(models.Model):
    nv_title=models.TextField(max_length=20,null=False, blank=False)
    nv_logo = models.ImageField(upload_to='logo/front')
    seo_title = models.TextField(max_length=200,null=True, blank=False)
    seo_description = models.TextField(max_length=500,null=True, blank=False)
    seo_keys=models.TextField(max_length=500,null=True, blank=False)

    def delete(self, *args, **kwargs):
        # Delete the image associated with the instance
        self.nv_logo.delete()
        # Call the superclass method
        super().delete(*args, **kwargs)