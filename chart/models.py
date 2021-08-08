from django.db import models


class TableOne(models.Model):
    # id = models.CharField(primary_key=True, max_length=30)
    xAxis = models.TextField()  # x轴数据
    yAxis = models.TextField()  # y轴数据
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     pass

    class Meta:
        db_table = 'table_one'  # 表名
        verbose_name = 'table_one'
        verbose_name_plural = verbose_name
        default_permissions = ()


class TableTwo(models.Model):
    # id = models.CharField(primary_key=True, max_length=30)
    xAxis = models.TextField()  # x轴数据
    yAxis = models.TextField()  # y轴数据
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'table_two'  # 表名
        verbose_name = 'table_two'
        verbose_name_plural = verbose_name
        default_permissions = ()
