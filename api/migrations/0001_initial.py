# Generated by Django 3.1.2 on 2020-10-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_axis', models.IntegerField(verbose_name='X')),
                ('y_axis', models.IntegerField(verbose_name='Y')),
                ('value', models.TextField(verbose_name='Value')),
            ],
        ),
    ]
