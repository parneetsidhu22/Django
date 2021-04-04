from django.db import models


class Blog(models.Model):
    msg = models.TextField()
