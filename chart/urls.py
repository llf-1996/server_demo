from django.urls import path, include
from rest_framework import routers

from chart.views import TableOneViewSet, TableTwoViewSet

router = routers.DefaultRouter()
router.register(r'table1', TableOneViewSet)
router.register(r'table2', TableTwoViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
