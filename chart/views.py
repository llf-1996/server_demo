import json

from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework.decorators import action

from chart.models import TableOne, TableTwo
from chart.serializers import TableOneSerializer, TableTwoSerializer
from chart.filters import TableOneFilter, TableTwoFilter
from utils.chart import random_data


class TableOneViewSet(viewsets.ModelViewSet):
    queryset = TableOne.objects.all()
    serializer_class = TableOneSerializer

    @action(methods=['get'], detail=False)
    def refresh(self, request):
        '''
        刷新图表数据
        '''
        try:
            data = random_data()
            obj = TableOne(yAxis=json.dumps(data))
            obj.save()
            res_data = {
                'data': data,
                'id': obj.id
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as e:
            print('>>>debug:', e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def latest(self, request):
    #     '''
    #     获取最近一条数据 get_or_create
    #     '''
    #     pass


class TableTwoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = TableTwo.objects.all()
    serializer_class = TableTwoSerializer
    filter_class = TableTwoFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['-id']

    @action(methods=['get'], detail=False)
    def data(self, request):
        '''
        保存当前图表数据
        '''
        id = request.query_params.get('id')
        try:
            table_one_obj = TableOne.objects.get(id=id)
            xAxis = table_one_obj.xAxis
            yAxis = table_one_obj.yAxis
            table_two_obj = TableTwo(xAxis=xAxis, yAxis=yAxis)
            table_two_obj.save()
            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            print('>>>debug:', e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
