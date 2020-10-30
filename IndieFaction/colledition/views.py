from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from . import serializers
from . import models

# Create your views here.
def HomeView(request):
    pass

class CEView(viewsets.ModelViewSet):
    queryset = models.CollectorEdition.objects.all()
    serializer_class = serializers.CollectorEditionSerializer

class CEGenreView(viewsets.ModelViewSet):
    queryset = models.CollectorsEditionGenre.objects.all()
    serializer_class = serializers.CollectorEditionGenreSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = models.Images.objects.all()
    serializer_class = serializers.ImageSerializer

@api_view(['GET','POST'])
def fetch_or_create_ce(request):
    if request.method=='GET':
        if len(request.GET)==1:
            try:
                ce_name = request.GET['collector_edition_name']
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.get(name=ce_name)
            except:
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(ce_objects)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_author(request):
    if request.method=='GET':
        if len(request.GET)==1:
            try:
                username = request.GET['username']
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(uid__username=username)
            except:
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(ce_objects,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_game_name(request):
    if request.method=='GET':
        if len(request.GET)==1:
            try:
                game_name = request.GET['game_name']
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(game_name=game_name)
            except:
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(ce_objects,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_random(request):
    if request.method=='GET':
        if len(request.GET)==1:
            try:
                n = int(request.GET['n'])
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.order_by('?')[:n]
            except Exception as e:
                print(e)
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(ce_objects,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_price(request):
    if request.method=='GET':
        if len(request.GET)==2:
            try:
               min_price  = request.GET['min_price']
               max_price  = request.GET['max_price']
            except:
                return JsonResponse({'code':400,'message':'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(price__lt=max_price,price__gt=min_price)
            except Exception as e:
                print(e)
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(ce_objects,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

