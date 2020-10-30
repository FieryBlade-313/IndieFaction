from . import models
from rest_framework import serializers

class IndieUserSerializer(serializers.ModelSerializer):
    date_of_joining = serializers.SerializerMethodField('get_doj')
    name = serializers.SerializerMethodField('get_name')

    class Meta:
        model = models.IndieUser
        fields = ('username','date_of_joining','profile_pic','name','website')

    def get_doj(self,obj):
        return obj.data_joined

    def get_name(self,obj):
        return {'first_name':obj.first_name,'middle_name':obj.middle_name,'last_name':obj.last_name}


