# Generated by Django 4.0 on 2022-01-27 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_articletag_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'ordering': ['-is_main', 'tag__name'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]
