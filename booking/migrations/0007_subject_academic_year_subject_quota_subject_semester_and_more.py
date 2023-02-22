# Generated by Django 4.1.1 on 2022-09-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_student_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='academic_year',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='subject',
            name='quota',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='subject',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=64),
        ),
    ]