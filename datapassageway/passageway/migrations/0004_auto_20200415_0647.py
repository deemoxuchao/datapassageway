# Generated by Django 2.2.4 on 2020-04-15 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passageway', '0003_importexport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexport',
            name='fagentnum',
            field=models.IntegerField(default=1, null=True, verbose_name='经销商编码'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fitermno',
            field=models.IntegerField(default=12, null=True, verbose_name='商品编号'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fqty',
            field=models.IntegerField(default=1, null=True, verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='ftoagentnum',
            field=models.IntegerField(default=1, null=True, verbose_name='去向单位'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='ftype',
            field=models.IntegerField(choices=[(0, '入库'), (1, '出库')], default=0, null=True, verbose_name='出/入'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='status',
            field=models.IntegerField(default=0, null=True, verbose_name='状态'),
        ),
    ]
