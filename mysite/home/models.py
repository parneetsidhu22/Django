from django.db import models


class Blogs(models.Model):
    msg = models.TextField()
