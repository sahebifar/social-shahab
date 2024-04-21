from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    bio = models.TextField(verbose_name="بایو", null=True, blank=True)
    photo = models.ImageField(verbose_name="تصویر", upload_to="account_images/", blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name="شغل", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='شماره تماس', null=True, blank=True)
