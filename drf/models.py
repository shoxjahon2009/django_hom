from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="Users", on_delete=models.CASCADE)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)

    def str(self):
        return self.name