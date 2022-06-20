# Generated by Django 4.0.5 on 2022-06-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0004_blockedusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='interests',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='surname',
            field=models.CharField(default='suname', max_length=50),
        ),
    ]