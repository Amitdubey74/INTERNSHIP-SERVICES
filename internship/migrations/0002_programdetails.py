# Generated by Django 4.2.3 on 2023-08-19 07:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programname', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=20)),
                ('fees', models.CharField(max_length=100)),
                ('startdate', models.DateField(default=django.utils.timezone.now)),
                ('enddate', models.DateField(default=django.utils.timezone.now)),
                ('perquisite', models.CharField(max_length=255)),
                ('stipend', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('Providerid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='internship.provider')),
            ],
        ),
    ]
