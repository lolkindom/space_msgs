# Generated by Django 3.1.7 on 2021-03-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_date', models.DateTimeField()),
                ('text', models.TextField()),
                ('is_read', models.BooleanField()),
            ],
        ),
    ]
