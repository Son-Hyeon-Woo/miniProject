# Generated by Django 2.2.5 on 2022-01-24 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placeboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='postname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=20, null=True)),
                ('date', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placeboard.Post')),
            ],
        ),
    ]
