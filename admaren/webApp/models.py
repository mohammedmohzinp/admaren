from django.db import models
from django.contrib.auth.models import User,auth
from taggit.managers import TaggableManager
# Create your models here.



class Snippet(models.Model):
    title           = models.CharField(max_length=100,default="",unique=True)
    sub_title       = models.CharField(max_length=100,default="")
    is_tag          = models.BooleanField(default=False)
    created_user    = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    snippet_tm      = models.TimeField(default="")
    snippet_dt      = models.DateField(default="")
    created         = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.validate_unique()
        super(Snippet,self).save(*args, **kwargs) 

class Tags(models.Model):
    snippet        = models.ForeignKey(Snippet,on_delete=models.CASCADE,default="")
    title          = TaggableManager()
    created        = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag


