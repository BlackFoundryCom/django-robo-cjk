# Generated by Django 3.2.4 on 2021-06-21 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robocjk', '0007_alter_font_designspace'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='atomicelementlayer',
            unique_together={('glif', 'group_name', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='characterglyphlayer',
            unique_together={('glif', 'group_name', 'name')},
        ),
    ]
