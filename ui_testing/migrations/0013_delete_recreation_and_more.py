# Generated by Django 4.2.7 on 2023-11-28 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui_testing', '0012_resumeexperienceblock_aggregate_line_skills_and_more'),
    ]

    operations = [
        # migrations.DeleteModel(
        #     name='Recreation',
        # ),
        # migrations.RemoveField(
        #     model_name='resumeexperienceblock',
        #     name='category',
        # ),
        # migrations.RemoveField(
        #     model_name='resumeline',
        #     name='line_skill_categories',
        # ),
        # migrations.RemoveField(
        #     model_name='resumeline',
        #     name='resume_experience_block',
        # ),
        # migrations.RemoveField(
        #     model_name='resumeskills',
        #     name='skill_category',
        # ),
        # migrations.DeleteModel(
        #     name='Web_Stack_Tools',
        # ),
        # migrations.DeleteModel(
        #     name='ResumeExperienceBlock',
        # ),
        # migrations.DeleteModel(
        #     name='ResumeExperienceCategory',
        # ),
        # migrations.DeleteModel(
        #     name='ResumeLine',
        # ),
        # migrations.DeleteModel(
        #     name='ResumeSkillCategories',
        # ),
        # migrations.DeleteModel(
        #     name='ResumeSkills',
        # ),

        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Recreation',
                ),
                migrations.RemoveField(
                    model_name='resumeexperienceblock',
                    name='category',
                ),
                migrations.RemoveField(
                    model_name='resumeline',
                    name='line_skill_categories',
                ),
                migrations.RemoveField(
                    model_name='resumeline',
                    name='resume_experience_block',
                ),
                migrations.RemoveField(
                    model_name='resumeskills',
                    name='skill_category',
                ),
                migrations.DeleteModel(
                    name='Web_Stack_Tools',
                ),
                migrations.DeleteModel(
                    name='ResumeExperienceBlock',
                ),
                migrations.DeleteModel(
                    name='ResumeExperienceCategory',
                ),
                migrations.DeleteModel(
                    name='ResumeLine',
                ),
                migrations.DeleteModel(
                    name='ResumeSkillCategories',
                ),
                migrations.DeleteModel(
                    name='ResumeSkills',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='recreation',
                    table='resume_recreation',
                ),
                migrations.AlterModelTable(
                    name='Web_Stack_Tools',
                    table='resume_webstacktools',
                ),
                migrations.AlterModelTable(
                    name='ResumeExperienceBlock',
                    table='resume_resumeexperienceblock',
                ),
                migrations.AlterModelTable(
                    name='ResumeExperienceCategory',
                    table='resume_resumeexperiencecategory',
                ),
                migrations.AlterModelTable(
                    name='ResumeSkillCategories',
                    table='resume_resumeskillcategories',
                ),
                migrations.AlterModelTable(
                    name='ResumeSkills',
                    table='resume_resumeskills',
                ),
            ],
        )

    ]