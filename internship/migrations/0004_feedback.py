# Generated by Django 4.2.3 on 2023-08-19 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0003_contactus_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('feedbacktext', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
