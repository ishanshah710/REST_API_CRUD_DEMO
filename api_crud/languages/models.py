from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
