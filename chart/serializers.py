from rest_framework import serializers

from chart.models import TableOne, TableTwo


class TableOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOne
        fields = '__all__'


class TableTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableTwo
        fields = '__all__'
