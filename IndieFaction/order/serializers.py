from rest_framework import serializers

from .models import PrintOrder, CompletedOrder


class PrintOrderSerializer(serializers.HyperlinkedModelSerializer):

    collector_edition_name = serializers.SerializerMethodField()

    class Meta:
        model = PrintOrder
        fields = ('collector_edition_name', 'status')

    def get_collector_edition_name(self, obj):
        collector_edition_name = obj.cid.name
        return collector_edition_name


class CompletedOrderSerializer(serializers.HyperlinkedModelSerializer):

    collector_edition_name = serializers.SerializerMethodField()

    class Meta:
        model = CompletedOrder
        fields = ('collector_eiditon_name', 'status')

    def get_collector_edition_name(self, obj):
        collector_edition_name = obj.cid.name
        return collector_edition_name
