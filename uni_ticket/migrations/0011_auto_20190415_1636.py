# Generated by Django 2.1.7 on 2019-04-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0010_auto_20190415_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='category',
        ),
        migrations.AddField(
            model_name='ticket',
            name='input_module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.TicketCategoryModule'),
            preserve_default=False,
        ),
    ]
