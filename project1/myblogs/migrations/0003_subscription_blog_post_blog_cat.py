# Generated by Django 5.0.1 on 2024-01-29 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0002_blog_post_alter_blog_category_blogcat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog_post',
            name='blog_cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_category'),
            preserve_default=False,
        ),
    ]
