from django.contrib.auth.models import User
from rest_framework import serializers

#import models from other apps
from education.models import Course
from experience.models import Job
from projects.models import Language,Project,ProjectLanguage
from userProfile.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
     class Meta:
          model = UserProfile
          fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
        class Meta:
             model =  Course
            #  fields = "__all__"

             fields = [ "name", "school", "school_url", "certificate", "certificate_image", "date_finished", "description"]
            
class JobSerializer(serializers.ModelSerializer):
     class Meta:
          model = Job
          fields = [ "title", "company_name", "company_link", "company_logo", "type", "description", "start_date", "end_date", "code_related"]

 
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "live_link", "code_link", "gif", 'languages', "course", "description","image","stack"]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [ "name", "link", "logo", "projects"]
        

class ProjectLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLanguage
        fields = [ "project", "language"]
        