# Generated by Django 3.2.9 on 2021-11-20 10:29

from django.db import migrations
import enumchoicefield.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=enumchoicefield.fields.EnumChoiceField(
                default=users.models.Role.EMPLOYEE, enum_class=users.models.Role, max_length=1),
        ),
    ]
