# Generated by Django 3.0.2 on 2020-01-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_widow', '0003_auto_20200129_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='webparsingjobmodel',
            name='json_file',
            field=models.CharField(default='---', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webparsingjobmodel',
            name='url',
            field=models.CharField(default='---', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='parsing_tags',
            field=models.CharField(choices=[('all_parse', 'All Tags'), ('relevant_parse', 'Relevant Tags (a, script, link, Form Tags)'), ('form_parse', 'Form Tags (form, input, textarea, select, option)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='parsing_type',
            field=models.CharField(choices=[('single_page', 'Single Page'), ('website_crawling', 'Website Crawling')], max_length=50),
        ),
    ]
