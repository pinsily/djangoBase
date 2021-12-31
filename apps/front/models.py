from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Profile(AbstractUser):
    index = models.BigAutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)
    nickname = models.CharField(verbose_name="昵称", max_length=256, default="", blank=True)

    status = models.IntegerField(verbose_name="状态", default=0, blank=True)
    version = models.IntegerField(verbose_name="版本号", default=0, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True, blank=True)

    class Meta:
        db_table = "profile"
        verbose_name = "用户表"
        app_label = "userprofile"
