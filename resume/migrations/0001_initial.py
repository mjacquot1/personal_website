# Generated by Django 4.2.7 on 2023-11-28 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Recreation',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('image_name', models.CharField(max_length=30)),
                        ('image_title', models.CharField(max_length=30)),
                        ('image_description', models.CharField()),
                        ('display_order', models.IntegerField(default=0)),
                        ('filter_field', models.CharField(choices=[('filter_ocean', 'Ocean'), ('filter_mountain', 'Mountain'), ('filter_misc', 'Misc'), ('filter_art', 'Art')], default='')),
                        ('main_image', models.ImageField(upload_to='recreation')),
                        ('tile_image', models.ImageField(upload_to='recreation')),
                    ],
                ),
                migrations.CreateModel(
                    name='ResumeExperienceCategory',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('category', models.CharField(max_length=50)),
                        ('display_order', models.IntegerField(default=0)),
                        ('category_display', models.CharField()),
                        ('icon_class', models.CharField(default='', max_length=30)),
                    ],
                ),
                migrations.CreateModel(
                    name='ResumeSkillCategories',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('category', models.CharField(max_length=50)),
                        ('display_order', models.IntegerField(default=0)),
                        ('category_display', models.CharField()),
                    ],
                ),
                migrations.CreateModel(
                    name='WebStackTools',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('tool_name', models.CharField(max_length=30)),
                        ('tool_description', models.CharField()),
                        ('tool_link', models.URLField()),
                        ('display_order', models.IntegerField(default=0)),
                        ('main_image', models.ImageField(upload_to='web_stack_icons')),
                    ],
                ),
                migrations.CreateModel(
                    name='ResumeSkills',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('skill_title', models.CharField(max_length=30)),
                        ('skill_years', models.FloatField(default=0)),
                        ('skill_filter_category', models.CharField(max_length=30)),
                        ('skill_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.resumeskillcategories')),
                    ],
                ),
                migrations.CreateModel(
                    name='ResumeExperienceBlock',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('title', models.CharField(max_length=100)),
                        ('company', models.CharField(blank=True, max_length=100)),
                        ('location', models.CharField(blank=True, max_length=100)),
                        ('sub_text', models.CharField(blank=True, max_length=100)),
                        ('start_date', models.DateField()),
                        ('end_date', models.DateField()),
                        ('still_there', models.BooleanField()),
                        ('lines', models.JSONField(default=dict)),
                        ('aggregate_line_skills', models.CharField(blank=True, default='')),
                        ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='resume.resumeexperiencecategory')),
                    ],
                ),
            ],
            # Table was already created. See ui_testing/migrations/0013
            database_operations=[],
        ),
    ]
    
