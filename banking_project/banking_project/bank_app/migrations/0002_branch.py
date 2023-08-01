# Generated by Django 4.2.3 on 2023-07-27 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='bank_app.district')),
            ],
        ),
    ]
