# Generated by Django 4.2.1 on 2023-05-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('d', 'Doctor'), ('p', 'Patient'), ('r', 'Receptionist'), ('a', 'Admin'), ('s', 'Staff')], default='p', max_length=20),
        ),
        migrations.DeleteModel(
            name='UserCategory',
        ),
    ]
