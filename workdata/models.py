from django.db import models

# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_html = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(max_length=200, null=True, blank=True)
    seniority_level = models.CharField(max_length=200, null=True, blank=True)
    job_function = models.CharField(max_length=200, null=True, blank=True)
    employment_type = models.CharField(max_length=200, null=True, blank=True)
    industries = models.CharField(max_length=200, null=True, blank=True)
    processed = models.BooleanField(default=False)

