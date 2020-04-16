# Generated by Django 2.2.4 on 2020-04-15 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportExport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fagentnum', models.IntegerField(verbose_name='经销商编码')),
                ('ftype', models.IntegerField(choices=[(0, '入库'), (1, '出库')], default=0, verbose_name='出/入')),
                ('fdatetime', models.DateTimeField(verbose_name='时间')),
                ('fitermno', models.IntegerField(verbose_name='商品编号')),
                ('fqty', models.IntegerField(verbose_name='商品数量')),
                ('ftoagentnum', models.IntegerField(verbose_name='去向单位')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
        ),
    ]
