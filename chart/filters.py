from django_filters import rest_framework as filters

from chart.models import TableOne, TableTwo


class TableOneFilter(filters.FilterSet):

    class Meta:
        model = TableOne
        fields = '__all__'


class TableTwoFilter(filters.FilterSet):

    class Meta:
        model = TableTwo
        fields = '__all__'
