# Generated by Django 3.0.8 on 2020-07-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcbn_cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='article_images'),
        ),
    ]