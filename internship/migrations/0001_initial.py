# Generated by Django 4.2.3 on 2023-08-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('providerid', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('provpass', models.CharField(max_length=45)),
                ('organizationname', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=45)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=100)),
                ('aboutorganisation', models.TextField()),
            ],
        ),
    ]
