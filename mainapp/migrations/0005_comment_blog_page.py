# Generated by Django 3.1.5 on 2021-03-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.blog'),
        ),
    ]
