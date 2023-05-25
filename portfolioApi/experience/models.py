from django.db import models

# Create your models here.
class Job(models.Model):
   
    JOB_TYPE_CHOICES = [
    ('INT', 'Internship'),
    ('VOL', 'Volunteer'),
    ('TMP', 'Temporary Contract'),
    ('IND', 'Indefinite'),
]

    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_link = models.URLField()
    company_logo = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=3, choices=JOB_TYPE_CHOICES, default="IND")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    code_related = models.BooleanField()

    def __str__(self):
        return self.company_name
