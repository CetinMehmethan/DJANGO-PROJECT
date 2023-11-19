from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="",blank=True,unique=True,max_length=50,db_index=True)

    def __str__(self):
        return f"{self.name}"


class events(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100,default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images",default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,editable=False,null=False,unique=True,db_index=True)
    isUpdated = models.BooleanField(default=1)
    categories = models.ManyToManyField(category)


    def save(self,*args,**kwargs):
        self.slug =slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title} {self.date}"

class slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active=models.BooleanField(default=False)
    events = models.ForeignKey(events,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.title}"
class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
    video = models.ImageField(upload_to="videos")
