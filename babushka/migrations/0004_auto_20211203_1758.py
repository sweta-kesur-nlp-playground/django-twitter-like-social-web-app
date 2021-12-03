# Generated by Django 3.2.9 on 2021-12-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babushka', '0003_post_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookUser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_reader',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username1',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
