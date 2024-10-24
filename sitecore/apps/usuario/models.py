from django.contrib.auth.models import AbstractUser
from django.db import models

from tenant.models import Tenant

class CustomUser(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
