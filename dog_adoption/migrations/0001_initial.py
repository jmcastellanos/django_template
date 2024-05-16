# Generated by Django 4.2.13 on 2024-05-16 03:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified_datetime', models.DateTimeField(auto_now=True)),
                ('original_name', models.CharField(max_length=128)),
                ('name', models.CharField(default=None, max_length=128, null=True)),
                ('birthday', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified_datetime', models.DateTimeField(auto_now=True)),
                ('birthday', models.DateField()),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
