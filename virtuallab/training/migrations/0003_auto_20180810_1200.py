# Generated by Django 2.0.7 on 2018-08-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='article',
            name='examples',
            field=models.TextField(default='example'),
        ),
    ]