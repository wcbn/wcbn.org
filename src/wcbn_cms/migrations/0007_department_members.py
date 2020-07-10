# Generated by Django 3.0.8 on 2020-07-10 20:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wcbn_cms', '0006_departmentmembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='members',
            field=models.ManyToManyField(through='wcbn_cms.DepartmentMembership', to=settings.AUTH_USER_MODEL),
        ),
    ]
