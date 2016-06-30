from django.db import models
from django.utils import timezone

class Alumnos(models.Model):

	nombre = models.CharField(max_length=200)
	nota = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)