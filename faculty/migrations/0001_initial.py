# Generated by Django 4.1.4 on 2022-12-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fno', models.IntegerField()),
                ('Fname', models.CharField(max_length=30)),
                ('Flastname', models.CharField(max_length=30)),
                ('Fdes', models.CharField(max_length=20)),
            ],
        ),
    ]
