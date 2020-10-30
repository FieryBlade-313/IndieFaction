from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse

from .models import PrintOrder, CompletedOrder


@api_view(['GET'])
def printOrder(request):

    if request.method == 'GET':
        if len(request.GET) == 1:
            try:
                token = request.GET['token']
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})
            try:
                order = PrintOrder.objects.get(token=token)
            except:
                return JsonResponse({'code': 404, 'message': 'Invalid Token'})
            serializer = PrintOrderSerializer(
                order, context={'request': request})
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def completedOrder(request):

    if request.method == 'GET':
        if len(request.GET) == 1:
            try:
                token = request.GET['token']
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})
            try:
                order = CompletedOrder.objects.get(token=token)
            except:
                return JsonResponse({'code': 404, 'message': 'Invalid Token'})
            serializer = PrintOrderSerializer(
                order, context={'request': request})
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})
