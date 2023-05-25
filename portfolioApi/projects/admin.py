from django.contrib import admin
from .models import Language,Project,ProjectLanguage
# Register your models here.
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(ProjectLanguage)
