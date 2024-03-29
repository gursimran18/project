# Generated by Django 3.1.2 on 2020-10-03 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_company', models.BooleanField(default=False)),
                ('is_developer', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('registerDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('currentJobName', models.CharField(max_length=255)),
                ('currentCompany', models.CharField(max_length=255)),
                ('developer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
                ('company_phone', models.IntegerField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
