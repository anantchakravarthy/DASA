# Generated by Django 4.1.3 on 2022-11-07 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('reason', models.CharField(choices=[('root_canal_treatment', 'Rot Canal Treatment'), ('impaction', 'Impaction'), ('tooth_pain', 'Tooth Pain'), ('cavity', 'Cavity'), ('filling', 'Filing'), ('crown_placement', 'Crown Placement')], max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('phone_number', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DentistLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ConsultationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('ConsultationDetails', models.CharField(max_length=500)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
            ],
        ),
    ]