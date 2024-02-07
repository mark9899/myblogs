# Generated by Django 5.0.1 on 2024-01-22 17:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('cover_img', models.ImageField(upload_to='images/')),
                ('blog_description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
