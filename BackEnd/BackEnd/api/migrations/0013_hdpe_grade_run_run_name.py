# Generated by Django 2.2.1 on 2019-06-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190629_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='hdpe_grade_run',
            name='Run_Name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
