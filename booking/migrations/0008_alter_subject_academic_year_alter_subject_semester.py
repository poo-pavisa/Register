# Generated by Django 4.1.1 on 2022-09-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_subject_academic_year_subject_quota_subject_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='academic_year',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(max_length=1),
        ),
    ]