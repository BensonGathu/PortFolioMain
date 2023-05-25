from django.urls import path
from mainApp import views


urlpatterns = [
    path('',views.get_endpoints,name = 'endpoints'),

   path('getUser/',views.user_profile,name="userprofile"),
   #Education urls
   path('education/',views.education_list,name="education"),
   path('education/<int:pk>/',views.education_details,name="educationdetails"),
   #job/experience urls
   path("experience/",views.experience_list,name="experience"),
   path("experience/<int:pk>/",views.experience_details,name="experiencedetails"),

   path("languages/",views.language_list,name="languages"),
   path("languages/<int:pk>/",views.language_details,name="languagedetails"),
   #Projects/l urls
   path("projects/",views.project_list,name="projects"),
   path("projects/<int:pk>/",views.project_details,name="projectsdetails"),

]