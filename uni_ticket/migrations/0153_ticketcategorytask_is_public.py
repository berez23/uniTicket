# Generated by Django 3.1.2 on 2020-10-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0152_task_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategorytask',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
