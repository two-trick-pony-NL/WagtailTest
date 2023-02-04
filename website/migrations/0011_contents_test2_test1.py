# Generated by Django 4.1.5 on 2023-02-04 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0010_organisationpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('title', models.TextField()),
                ('Contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='website.contents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('Contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='website.contents')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
