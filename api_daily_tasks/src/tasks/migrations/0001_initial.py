# Generated by Django 4.0.4 on 2022-05-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('status', models.IntegerField(choices=[(0, 'To-do'), (1, 'Doing'), (2, 'Finished')])),
            ],
        ),
    ]
