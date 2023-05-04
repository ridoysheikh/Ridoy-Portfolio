# Generated by Django 4.1.5 on 2023-02-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0007_edu_cat_educations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=2)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Front_Pages.skill_cat')),
            ],
        ),
    ]
