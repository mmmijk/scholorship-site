# Generated by Django 2.2.7 on 2019-12-21 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0008_auto_20191221_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='filemanager.Rate', verbose_name='得分'),
        ),
    ]