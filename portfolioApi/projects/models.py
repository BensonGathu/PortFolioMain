from django.db import models
from education.models import Course

class Language(models.Model):
    """ Save language details """
    name = models.CharField(max_length=100)
    link = models.URLField( blank=True, null=True,)
    logo = models.URLField( blank=True, null=True,)

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Save project details """

    title = models.CharField(max_length=100)
    live_link = models.URLField()
    code_link = models.URLField()
    gif = models.FileField(upload_to='gifs/',blank=True, null=True,)
    course = models.ForeignKey(Course, blank=True, null=True, related_name='projects', on_delete=models.SET_NULL)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    stack = models.CharField(max_length=100,blank=True, null=True,)
    languages = models.ManyToManyField(Language, through='ProjectLanguage', related_name="projects")


    def __str__(self):
        return self.title


class ProjectLanguage(models.Model):
    """ Connect Project model to Language model """
    class Meta:
        """
        Ensure each project/language pairing can only be added to each list once.
        """
        constraints = [models.UniqueConstraint(fields=["project", "language"], name='unique_pairing')]

    project = models.ForeignKey(Project, related_name="project_languages", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name="project_languages", on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + " - " + self.language.name
