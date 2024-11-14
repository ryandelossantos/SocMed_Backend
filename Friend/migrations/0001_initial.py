# Generated by Django 5.1.2 on 2024-11-13 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_user_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_user_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_1', 'user_2')},
            },
        ),
    ]