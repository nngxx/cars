# Generated by Django 4.0.3 on 2022-03-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('engine', models.FloatField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('cost', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'samochody',
                'verbose_name_plural': 'Samochody',
            },
        ),
    ]