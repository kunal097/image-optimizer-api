from django.db import models
from django.core.validators import URLValidator
from image_optmizer.settings import MEDIA_ROOT
import requests
from django.contrib.auth.models import User

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
        try:
            r = requests.get(self.url)
        except:
            pass

        if r.status_code == 200:
            self.local_path = MEDIA_ROOT + '/upload/' + self.url.split('/')[-1]



            with open(self.local_path,
                      'wb') as f:
                f.write(r.content)

        super(Image,self).save(*args,**kwargs)




class Temp_User(models.Model):
    ip_address = models.CharField(max_length=15)
    count = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False )


    def __str__(self):
        return self.ip_address


class AuthToken(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    api_key = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.api_key
