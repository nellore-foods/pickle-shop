from django.conf import settings
from django.db import models


class BaseUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    location = models.CharField(max_length=63)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    active = models.BooleanField()

    class Meta:
        abstract = True


class Customer(BaseUser):
    first_name = models.CharField(max_length=63)
    middle_name = models.CharField(max_length=63, null=True, blank=True)
    last_name = models.CharField(max_length=63, null=True, blank=True)

    def __repr__(self):
        return (
            f"Customer[ "
                f"ID: {self.id}, ",
                f"User: {self.user}, ",
                f"First Name: {self.first_name}, ",
                f"Middle Name: {self.middle_name},  ",
                f"Last Name: {self.last_name},  ",
                f"Location: {self.location},  ",
                f"Address: {self.address},  ",
                f"Phone: {self.phone},  ",
                f"Active: {self.active},  ",
            f"]"
        )

    def __str__(self):
        return (
            f"{self.first_name} {self.middle_name} {self.last_name} from ",
            f"{self.location}"
        )


class Outlet(BaseUser):
    name = models.CharField(max_length=63)

    def __repr__(self):
        return (
            f"Outlet[ "
                f"ID: {self.id}, ",
                f"User: {self.user}, ",
                f"Name: {self.name},  ",
                f"Location: {self.location},  ",
                f"Address: {self.address},  ",
                f"Phone: {self.phone},  ",
                f"Active: {self.active},  ",
            f"]"
        )

