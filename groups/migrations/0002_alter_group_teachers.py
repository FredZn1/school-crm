# Generated by Django 5.1.4 on 2025-01-11 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('teachers', '0002_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teachers',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_teacher', to='teachers.teacher'),
        ),
    ]
