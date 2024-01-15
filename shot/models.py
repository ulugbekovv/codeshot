from django.db import models


class Generations(models.Model):
    ip = models.GenericIPAddressField()
    image = models.ImageField(upload_to='generations/')