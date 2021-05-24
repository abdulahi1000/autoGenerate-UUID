from django.db import models
import uuid

# Create your models here.


class UserDetails(models.Model):
    TimeStamp = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    def __str__(self):
        return str(self.user_id)
