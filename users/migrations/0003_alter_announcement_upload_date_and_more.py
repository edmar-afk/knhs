# Generated by Django 5.0.4 on 2024-05-23 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_announcement_upload_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 8, 0, 59, 308886, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 8, 0, 59, 308886, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 8, 0, 59, 308886, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 8, 0, 59, 308886, tzinfo=datetime.timezone.utc)),
        ),
    ]