# Generated by Django 5.2.2 on 2025-06-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bg_image', models.ImageField(upload_to='assets/img')),
                ('prof_image', models.ImageField(upload_to='assets/img')),
                ('position', models.CharField(max_length=100)),
                ('description_about', models.TextField()),
                ('description_position', models.TextField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='assets/files')),
                ('experience', models.IntegerField(default=0)),
                ('project_success', models.IntegerField(default=0)),
                ('satisfication_rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('certification', models.CharField(blank=True, max_length=100, null=True)),
                ('field_of_study', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, default='Present', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, default='Present', null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='assets/img')),
                ('source_code', models.URLField(blank=True, null=True)),
                ('view_project', models.URLField(blank=True, null=True)),
                ('page_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField()),
            ],
        ),
    ]
