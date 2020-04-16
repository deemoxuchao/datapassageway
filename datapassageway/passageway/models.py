from django.db import models
from django.utils.timezone import now


class ImportExport(models.Model):
    id = models.AutoField(primary_key=True)
    fagentnum = models.CharField('经销商编码', max_length=50, null=True)
    ftype = models.CharField('出/入', max_length=10, null=True)
    fdatetime = models.DateTimeField('时间', null=True)
    fitermno = models.CharField('商品编号', max_length=50, null=True)
    fqty = models.IntegerField('商品数量', null=True)
    ftoagentnum = models.CharField('去向单位', max_length=50, null=True)
    status = models.IntegerField('状态', null=True)
    created_time = models.DateTimeField('创建时间', default=now, null=True)
    last_mod_time = models.DateTimeField('修改时间', default=now, null=True)

