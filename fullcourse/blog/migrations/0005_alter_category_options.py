# Generated by Django 4.0.5 on 2022-07-16 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_parent_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]