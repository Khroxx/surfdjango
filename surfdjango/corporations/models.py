from django.db import models
from surfdjango.users.models import User

# Create your models here.


class Corporation(models.Model):
    name = models.CharField(max_length=255, required=True)
    adress = models.TextField(max_length=255, required=True)
    url = models.URLField(default=None, blank=True, null=True)
    # other = models.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='corporations')
    