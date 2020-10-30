from rest_framework import serializers
from .models import CollectorEdition,CollectorsEditionGenre,Images


class CollectorEditionSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField('get_created_by')
    genre = serializers.SerializerMethodField('get_genre')
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = CollectorEdition
        fields = ['name','price','no_of_content','date_of_creation','genre','thumbnail','game_name','created_by']

    def get_created_by(self,obj):
        return obj.uid.username

    def get_genre(self,obj):
        val = [x.genre_name for x in obj.genre.all()]
        return val

    def get_thumbnail(self,obj):
        val = [x.url_thumbnail for x in obj.images.all()]
        return val


class CollectorEditionGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectorsEditionGenre
        fields = ['genre_name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['img_id']
