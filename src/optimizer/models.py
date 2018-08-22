from django.db import models
from django.core.validators import URLValidator
from image_optmizer.settings import MEDIA_ROOT
import requests

# Create your models here.

class Image(models.Model):
    url = models.TextField(max_length=200,blank=False,validators=[URLValidator()])
    quality = models.IntegerField(blank=False)
    dimension = models.FloatField(blank=True,null=True)
    local_path = models.CharField(max_length=50,blank=True)

    def __str__(self):
        if self.local_path:
            return str(self.local_path)
        else:
            return str(self.url)


    def save(self,*args,**kwargs):
        r = requests.get(self.url)

        if r.status_code == 200:
            self.local_path = MEDIA_ROOT + '/upload/' + self.url.split('/')[-1]



            with open(self.local_path,
                      'wb') as f:
                f.write(r.content)

        super(Image,self).save(*args,**kwargs)


