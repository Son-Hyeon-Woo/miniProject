# Generated by Django 2.2.5 on 2022-01-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
        migrations.AddField(
            model_name='post',
            name='top_fixed',
            field=models.BooleanField(default=False, verbose_name='상단고정'),
        ),
    ]
