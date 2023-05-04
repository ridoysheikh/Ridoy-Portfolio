# Generated by Django 4.1.5 on 2023-02-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0006_social_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='edu_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='educations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('institute', models.CharField(max_length=50)),
                ('start_year', models.CharField(max_length=10)),
                ('end_year', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Front_Pages.edu_cat')),
            ],
        ),
    ]
