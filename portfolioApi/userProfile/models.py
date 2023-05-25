from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.username}'


# class Media(models.Model):

#     class Meta:
#         verbose_name_plural = 'Media Files'
#         verbose_name = 'Media'
#         ordering = ["name"]
	
#     image = models.ImageField(blank=True, null=True, upload_to="media")
#     url = models.URLField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     is_image = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if self.url:
#             self.is_image = False
#         super(Media, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.name
