# Generated by Django 3.2.6 on 2021-08-05 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210805_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
