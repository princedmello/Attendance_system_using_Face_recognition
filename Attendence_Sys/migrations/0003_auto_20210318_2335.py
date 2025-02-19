# Generated by Django 3.1.7 on 2021-03-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence_Sys', '0002_auto_20210318_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200, null=True)),
                ('count', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('percentage', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='count',
        ),
        migrations.RemoveField(
            model_name='student',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='student',
            name='total',
        ),
    ]
