# Generated by Django 4.0.5 on 2022-07-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته بندی'),
        ),
    ]
