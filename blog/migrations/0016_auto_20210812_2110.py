# Generated by Django 3.2.6 on 2021-08-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]