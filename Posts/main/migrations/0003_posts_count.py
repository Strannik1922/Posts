# Generated by Django 4.1.7 on 2023-04-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_posts_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
