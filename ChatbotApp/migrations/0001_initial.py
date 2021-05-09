# Generated by Django 3.1.7 on 2021-05-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('userName', models.CharField(max_length=10)),
                ('stdNum', models.CharField(max_length=13)),
                ('userEmail', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]