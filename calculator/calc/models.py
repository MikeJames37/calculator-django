from django.db import models
from django.urls import reverse


class Calculator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('calc', kwargs={'calc_slug': self.slug})