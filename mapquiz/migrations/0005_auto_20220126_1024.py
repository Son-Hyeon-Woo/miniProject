# Generated by Django 2.2.5 on 2022-01-26 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapquiz', '0004_auto_20220125_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizlog',
            name='user_id',
        ),
        migrations.AddField(
            model_name='quizlog',
            name='user',
            field=models.ForeignKey(db_column='username', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
