# Generated by Django 4.1.6 on 2023-02-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profit', models.CharField(max_length=10)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
    ]
