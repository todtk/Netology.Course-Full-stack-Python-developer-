# Generated by Django 4.1.2 on 2023-01-19 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
