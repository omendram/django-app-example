# Generated by Django 3.1.4 on 2020-12-27 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201227_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlaySession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='last_played',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.game'),
        ),
    ]
