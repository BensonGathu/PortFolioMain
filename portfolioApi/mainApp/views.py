from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
# Import our serializers
from mainApp.serializers import UserSerializer,UserProfileSerializer,CourseSerializer,JobSerializer,ProjectSerializer,LanguageSerializer,ProjectLanguageSerializer
from rest_framework.decorators import api_view

#import models from other apps
from education.models import Course
from experience.models import Job
from projects.models import Language,Project,ProjectLanguage
from userProfile.models import UserProfile

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(["GET"])
def get_endpoints(request):
	data =["test"]
	return Response(data)
#User related info
@csrf_exempt
def user_profile(request):
	#Get user profile
	if request.method == 'GET':
		data = UserProfile.objects.all()
		serializer = UserProfileSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UserProfileSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

#Education related info
@csrf_exempt
def education_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def education_details(request,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=204)

#Experience related info
@csrf_exempt
def experience_list(request):
    if request.method == 'GET':
        experience = Job.objects.all()
        serializer = JobSerializer(experience,many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def experience_details(request,pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = JobSerializer(job)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JobSerializer(job, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        job.delete()
        return HttpResponse(status=204)
    

#Project/languages related info
    #languages related info
@csrf_exempt
def language_list(request):
    if request.method == 'GET':
        language = Language.objects.all()
        serializer = LanguageSerializer(language,many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def language_details(request,pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(language, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        language.delete()
        return HttpResponse(status=204)
    


    #projects related info
@csrf_exempt
def project_list(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(project,many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def project_details(request,pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=204)
    

    


