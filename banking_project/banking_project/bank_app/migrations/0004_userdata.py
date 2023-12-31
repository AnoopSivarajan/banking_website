# Generated by Django 4.2.3 on 2023-07-31 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0003_district_wiki_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('account_type', models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account'), ('NRI Account', 'NRI Account')], max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.district')),
            ],
        ),
    ]
