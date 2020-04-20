from django.db import models

# Create your models here.


class RepoList(models.Model):
    repo = models.CharField(max_length=500)
