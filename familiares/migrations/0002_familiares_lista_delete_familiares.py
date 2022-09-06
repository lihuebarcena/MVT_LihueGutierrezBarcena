# Generated by Django 4.1 on 2022-09-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='familiares_lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('year_born', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='familiares',
        ),
    ]