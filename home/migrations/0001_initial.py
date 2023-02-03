# Generated by Django 4.1.5 on 2023-02-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='team')),
                ('name', models.CharField(max_length=200)),
                ('job', models.CharField(default='Developer', max_length=200)),
                ('linkedin', models.CharField(blank=True, max_length=500, null=True)),
                ('github', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
