from django.shortcuts import render
from . import serializers
from . import models
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def IndieUserView(request):
    if request.method == 'GET':
        # print((request.GET))
        if len(request.GET)==1:
            try:
                user_name = request.GET['username']
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})
            try:
                user_obj = models.IndieUser.objects.get(username=user_name)
            except:
                return JsonResponse({'code':404,'message':'User does not exist'})
            serializer = serializers.IndieUserSerializer(user_obj)
            return Response(serializer.data)
        else:
            return JsonResponse({'code':400,'message':'Bad Input Parameter'})