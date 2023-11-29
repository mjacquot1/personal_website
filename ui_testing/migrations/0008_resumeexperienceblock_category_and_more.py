# Generated by Django 4.2.7 on 2023-11-22 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui_testing', '0007_resumeexperiencecategory_icon_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeexperienceblock',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='ui_testing.resumeexperiencecategory'),
        ),
        migrations.AlterField(
            model_name='recreation',
            name='filter_field',
            field=models.CharField(choices=[('filter_art', 'Art'), ('filter_ocean', 'Ocean'), ('filter_mountain', 'Mountain'), ('filter_misc', 'Misc')], default=''),
        ),
    ]
