# Generated by Django 2.2.7 on 2019-12-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('latitude', models.DecimalField(decimal_places=10, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=19)),
                ('usi', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('shift', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('age', models.CharField(blank=True, max_length=200)),
                ('pfc', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('sl', models.CharField(max_length=200)),
                ('running', models.BooleanField(blank=True, default=True)),
                ('chasing', models.BooleanField(blank=True, default=True)),
                ('climbing', models.BooleanField(blank=True, default=True)),
                ('eating', models.BooleanField(blank=True, default=True)),
                ('foraging', models.BooleanField(blank=True, default=True)),
                ('oa', models.CharField(blank=True, max_length=200)),
                ('kuks', models.BooleanField(blank=True, default=True)),
                ('quaas', models.BooleanField(blank=True, default=True)),
                ('moans', models.BooleanField(blank=True, default=True)),
                ('tf', models.BooleanField(blank=True, default=True)),
                ('tt', models.BooleanField(blank=True, default=True)),
                ('approaches', models.BooleanField(blank=True, default=True)),
                ('indifferent', models.BooleanField(blank=True, default=True)),
                ('rf', models.BooleanField(blank=True, default=True)),
            ],
        ),
    ]
