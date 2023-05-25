from django.db import models

# Create your models here.
class Course(models.Model):
    """ Save course info """
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    school_url = models.URLField()
    certificate = models.BooleanField()
    certificate_image = models.URLField(null=True, blank=True)
    date_finished = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name + " - " + self.school
