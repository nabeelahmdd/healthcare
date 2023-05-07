# Generated by Django 4.2.1 on 2023-05-07 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_availabilitiy_appointment_availabilitiy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitiy',
            name='cr_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='availabilitiy_cr_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='availabilitiy',
            name='up_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='availabilitiy_up_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
