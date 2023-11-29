# Generated by Django 4.2.7 on 2023-11-22 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_testing', '0008_resumeexperienceblock_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeexperienceblock',
            name='sub_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='recreation',
            name='filter_field',
            field=models.CharField(choices=[('filter_mountain', 'Mountain'), ('filter_misc', 'Misc'), ('filter_ocean', 'Ocean'), ('filter_art', 'Art')], default=''),
        ),
        migrations.AlterField(
            model_name='resumeexperienceblock',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resumeexperienceblock',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resumeexperienceblock',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
