from django.db import models
import uuid


class UserDetails(models.Model):

    class Meta:
        db_table = '"dashboard_user"'
    ROLES = [('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin'), ('editor', 'Editor')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
