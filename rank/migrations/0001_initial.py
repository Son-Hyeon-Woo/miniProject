# Generated by Django 2.2.5 on 2022-01-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Around_place',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('id_p', models.IntegerField()),
            ],
            options={
                'db_table': 'around_place',
                'managed': False,
            },
        ),
    ]
