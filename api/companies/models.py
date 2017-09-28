from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    class Meta:
        db_table = 'company'

    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=64, null=False)
