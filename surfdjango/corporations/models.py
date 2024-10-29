from django.db import models

from surfdjango.users.models import User

# Create your models here.


class Corporation(models.Model):
    """
    Default Corporation Model.
    Add fields if necessary.
    """

    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=255, blank=False, null=False)
    url = models.URLField(default=None, blank=True)
    # other = models.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="corporations",
    )

    def __str__(self):
        return f"{self.name}"
