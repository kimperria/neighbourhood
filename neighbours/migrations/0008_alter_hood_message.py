# Generated by Django 4.0.3 on 2022-04-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0007_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='message',
            field=models.TextField(default='Tell us a little bit about yourself'),
        ),
    ]