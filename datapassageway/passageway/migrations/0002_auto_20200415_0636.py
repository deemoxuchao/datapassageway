# Generated by Django 2.2.4 on 2020-04-15 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passageway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexport',
            name='fagentnum',
            field=models.IntegerField(default=1, verbose_name='经销商编码'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fitermno',
            field=models.IntegerField(default=12, verbose_name='商品编号'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='fqty',
            field=models.IntegerField(default=1, verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='ftoagentnum',
            field=models.IntegerField(default=1, verbose_name='去向单位'),
        ),
    ]
