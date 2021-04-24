# Generated by Django 3.1 on 2021-04-22 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(choices=[('taxi', 'Taxi'), ('car', 'Car'), ('on foot', 'On foot'), ('bike', 'Bike')], max_length=30)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('transport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='transport.transport')),
                ('initial_node', models.CharField(max_length=100)),
                ('final_node', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('transport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='transport.transport')),
                ('departure_time', models.TimeField()),
            ],
        ),
    ]
