# Generated by Django 3.0.8 on 2020-08-02 17:06

from django.db import migrations
import wcbn_util.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wcbn_cms', '0005_auto_20200802_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='featured_image_caption',
            field=wcbn_util.fields.CharField(blank=True, max_length=65000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='featured_image_caption',
            field=wcbn_util.fields.CharField(blank=True, max_length=65000, null=True),
        ),
    ]
