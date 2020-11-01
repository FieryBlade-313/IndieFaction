import json
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from . import serializers
from . import models
from accounts.models import IndieUser

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


@api_view(['GET', 'POST'])
def fetch_or_create_ce(request):
    if request.method == 'GET':
        return fetch_ce(request)
    if request.method == 'POST':
        return create_ce(request)


def fetch_ce(request):
    if len(request.GET) == 1:
        try:
            ce_name = request.GET['collector_edition_name']
        except:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

        try:
            ce_objects = models.CollectorEdition.objects.get(name=ce_name)
        except:
            return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
        serializer = serializers.CollectorEditionSerializer(ce_objects)
        return Response(serializer.data)
    else:
        return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


def create_ce(request):
    data = json.loads(request.body.decode('utf-8'))
    if len(data) == 7:
        required_keys = ['username', 'token', 'price',
                         'game_name', 'genre', 'image_url', 'collector_name']
        for required_key in required_keys:
            if required_key not in data:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

        try:
            user_data = IndieUser.objects.get(
                username=data['username'], token=data['token'])
            try:
                models.CollectorEdition.objects.get(
                    name=data['collector_name'])
                return JsonResponse({'code': 409, 'message': 'Collector Edition Already Exists'})
            except:
                # Save collector edition
                cedition = models.CollectorEdition(
                    name=data['collector_name'], price=data['price'], game_name=data['game_name'], uid=user_data)
                cedition.save()
                for image in data['image_url']:
                    img = models.Images(
                        url_thumbnail=image, url_high_res=image)
                    img.save()
                    cedition.images.add(img)
                for genre in data['genre']:
                    try:
                        cedition.genre.add(
                            models.CollectorsEditionGenre.objects.get(genre_name=genre))
                    except:
                        pass
                cedition.save()
                return JsonResponse({'code': 200, 'message': 'Collector Edition created Successfuly'})
        except:
            return JsonResponse({'code': 404, 'message': 'Invalid Token or username'})

    else:
        return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['PUT'])
def edit_ce(request):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        if 'collector_edition_name' in data:
            try:
                cedition = models.CollectorEdition.objects.get(
                    name=data['collector_edition_name'])
                try:
                    user_data = IndieUser.objects.get(
                        username=data['username'], token=data['token'])
                except:
                    return JsonResponse({'code': 409, 'message': 'Invalid Username or Token'})
                if user_data.uid != cedition.uid.uid:
                    return JsonResponse({'code': 409, 'message': 'Not authorized to edit the collector edition'})
                else:
                    if 'edit_data' in data:
                        edit_data = data['edit_data']
                        if 'collector_edition_name' in edit_data:
                            try:
                                models.CollectorEdition.objects.get(
                                    name=edit_data['collector_edition_name'])
                                return JsonResponse({'code': 409, 'message': 'Collector Edition Already Exists by the given edit name'})
                            except:
                                cedition.name = edit_data['collector_edition_name']
                        if 'price' in edit_data:
                            cedition.price = edit_data['price']
                        if 'add_genre' in edit_data:
                            for genre in edit_data['add_genre']:
                                try:
                                    cedition.genre.add(
                                        models.CollectorsEditionGenre.objects.get(genre_name=genre))
                                except:
                                    pass
                        if 'rem_genre' in edit_data:
                            all_genre = [
                                x.genre_name for x in cedition.genre.all()]
                            for genre in edit_data['rem_genre']:
                                try:
                                    if genre in all_genre:
                                        cedition.genre.remove(
                                            models.CollectorsEditionGenre.objects.get(genre_name=genre))
                                except:
                                    pass
                        if 'add_image_url' in edit_data:
                            all_images = [
                                x.url_thumbnail for x in cedition.images.all()]
                            for image in edit_data['add_image_url']:
                                if image not in all_images:
                                    img = models.Images(
                                        url_thumbnail=image, url_high_res=image)
                                    img.save()
                                    cedition.images.add(img)
                        cedition.save()
                        return JsonResponse({'code': 200, 'message': 'Edited Collector Edition Successfuly'})
                    else:
                        return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})
            except:
                return JsonResponse({'code': 404, 'message': 'Invalid Collector edition'})


@api_view(['GET'])
def fetch_ce_author(request):
    if request.method == 'GET':
        if len(request.GET) == 1:
            try:
                username = request.GET['username']
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(
                    uid__username=username)
            except:
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(
                ce_objects, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_game_name(request):
    if request.method == 'GET':
        if len(request.GET) == 1:
            try:
                game_name = request.GET['game_name']
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(
                    game_name=game_name)
            except:
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(
                ce_objects, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_random(request):
    if request.method == 'GET':
        if len(request.GET) == 1:
            try:
                n = int(request.GET['n'])
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.order_by('?')[:n]
            except Exception as e:
                print(e)
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(
                ce_objects, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})


@api_view(['GET'])
def fetch_ce_price(request):
    if request.method == 'GET':
        if len(request.GET) == 2:
            try:
                min_price = request.GET['min_price']
                max_price = request.GET['max_price']
            except:
                return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})

            try:
                ce_objects = models.CollectorEdition.objects.filter(
                    price__lt=max_price, price__gt=min_price)
            except Exception as e:
                print(e)
                return JsonResponse({'code': 404, 'message': 'Collector Edition does not exist'})
            serializer = serializers.CollectorEditionSerializer(
                ce_objects, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'code': 400, 'message': 'Bad Input Parameter'})
