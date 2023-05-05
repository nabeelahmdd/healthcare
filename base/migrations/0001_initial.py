# Generated by Django 4.2.1 on 2023-05-05 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50)),
                ('soft_delete', models.BooleanField(default=False)),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='specialty_cr_by', to=settings.AUTH_USER_MODEL)),
                ('up_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='specialty_up_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('medical_history', models.TextField()),
                ('allergies', models.TextField()),
                ('current_medications', models.TextField()),
                ('blood_type', models.CharField(max_length=5)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('soft_delete', models.BooleanField(default=False)),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='medical_record_cr_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('up_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='medical_record_up_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_delete', models.BooleanField(default=False)),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='doctor_cr_by', to=settings.AUTH_USER_MODEL)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.specialty')),
                ('up_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='doctor_up_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('R', 'Rescheduled'), ('X', 'Cancelled')], max_length=1)),
                ('reason', models.TextField()),
                ('soft_delete', models.BooleanField(default=False)),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointment_cr_by', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('up_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointment_up_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
