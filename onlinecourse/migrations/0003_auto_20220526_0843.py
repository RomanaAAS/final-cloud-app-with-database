# Generated by Django 3.1.3 on 2022-05-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220526_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.TextField(default='possible answer', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=100),
        ),
    ]
