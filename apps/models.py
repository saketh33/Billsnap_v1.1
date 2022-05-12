from django.db import models

class applists(models.Model):
    appname=models.CharField(verbose_name='App name',primary_key=True,max_length=50,unique=True,null=False)
    appimg=models.ImageField(upload_to = 'app_images',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='created date',auto_now_add=True,editable=False,null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated date',null=True,blank=True)

    def __str__(self):
        return str(self.appname)

    def save(self, *args, **kwargs):
        super(applists, self).save()


class customer(models.Model):

    #utility details
    utility_name = models.CharField(max_length=200, null=True, blank=True)
    utility_short_name= models.CharField(max_length=50, null=True, blank=True)
    utility_state= models.CharField(max_length=50, null=True, blank=True)
    utility_district= models.CharField(max_length=50, null=True, blank=True)
    utility_country= models.CharField(max_length=50, null=True, blank=True)
    utility_postalcode= models.CharField(max_length=20, null=True, blank=True)

    #contact details
    person= models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    ph_num = models.CharField(max_length=15, null=True, blank=True)
    designation= models.CharField(max_length=100, null=True, blank=True)

    #contact details

    info_created_at = models.DateTimeField(auto_now_add=True)
    info_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name