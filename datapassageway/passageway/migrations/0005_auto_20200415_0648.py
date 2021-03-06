# Generated by Django 2.2.4 on 2020-04-15 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passageway', '0004_auto_20200415_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexport',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='importexport',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='修改时间'),
        ),
    ]
