# Generated by Django 4.1.7 on 2023-03-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_hero_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60)),
            ],
        ),
    ]
