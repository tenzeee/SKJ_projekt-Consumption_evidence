# Generated by Django 3.2 on 2021-05-04 19:46

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
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('motor', models.CharField(max_length=80, null=True)),
                ('fuel', models.CharField(max_length=50)),
                ('fuelTank', models.FloatField()),
                ('kilometresCount', models.FloatField()),
                ('refuelCount', models.IntegerField(default=0)),
                ('longTermConsumption', models.FloatField(default=0)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometresCount', models.FloatField()),
                ('fuelType', models.CharField(max_length=20)),
                ('liters', models.FloatField()),
                ('pricePerLiter', models.FloatField()),
                ('price', models.FloatField()),
                ('fullTank', models.BooleanField(default=False)),
                ('fuelTankActualState', models.FloatField()),
                ('shortTermConsumption', models.FloatField(default=0)),
                ('missingRecord', models.BooleanField(default=False)),
                ('refuelDate', models.DateTimeField(auto_now_add=True, verbose_name='refueled')),
                ('tankStation', models.CharField(max_length=255, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vehicle')),
            ],
        ),
    ]
