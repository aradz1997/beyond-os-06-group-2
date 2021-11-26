# Generated by Django 3.2.9 on 2021-11-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='assigneeTasks',
                                    to='users.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='createdTasks',
                                    to='users.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='tasks.task', related_name='task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='appUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appUser',
                                    to='users.user'),
        ),
    ]
