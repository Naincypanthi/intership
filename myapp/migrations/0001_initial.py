# Generated by Django 4.2.10 on 2024-02-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=20)),
                ('date', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
