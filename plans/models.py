from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import string
import random
from django.utils.text import slugify

def generate_code():
    length=10
    base = string.ascii_lowercase+string.ascii_uppercase+string.digits
    while True:
        code = ''.join(random.choices(base, k=length))
        if Plan.objects.filter(slug=code).count()==0:
            break
    return code

def default_generate_code():
    length=10
    base = string.ascii_lowercase+string.ascii_uppercase+string.digits
    while True:
        code = ''.join(random.choices(base, k=length))
        if Plan.objects.filter(slug=code).count()==0:
            break
    return code

def dummy_generate_code():
    length=10
    base = string.ascii_lowercase+string.ascii_uppercase+string.digits
    while True:
        code = ''.join(random.choices(base, k=length))
        if Plan.objects.filter(slug=code).count()==0:
            break
    return code


class Plan(models.Model):
    slug = models.CharField(max_length=20, default=generate_code, editable=False)
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=800)
    duration = models.IntegerField(default=30, choices=[
            (30, '1 Month'),
            (180, '6 Months'),
            (364, '1 Year')
        ],
    )
    is_dummy = models.BooleanField(default=False)
    default_for_everyone = models.BooleanField(default=False)

    def __str__(self):
        plan_type = 'Default'
        if self.is_dummy:
            plan_type = 'Dummy'
        return f"[{self.title}] Plan at [Rs.{self.price}] for [{self.duration} days] [{plan_type}]"
    