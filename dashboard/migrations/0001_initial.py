# Generated by Django 3.2 on 2024-01-20 11:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin'), ('editor', 'Editor')], max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': '"dashboard_user"',
            },
        ),
    ]
