# Generated by Django 2.2.7 on 2019-12-21 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0006_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanager.Rate', verbose_name='得分'),
        ),
    ]
