from django.db import models
import uuid


def _get_avatar_filename(instance, filename):
    """Use random filename prevent overwriting existing files & to fix caching issues."""
    return f'profile-pictures/{uuid.uuid4()}.{filename.split(".")[-1]}'


# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.FileField(upload_to=_get_avatar_filename, blank=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return "%s" % (self.first_name)
