# Generated by Django 3.1 on 2020-09-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                (
                    'action',
                    models.CharField(
                        choices=[
                            ('L', 'liked'),
                            ('F', 'followed'),
                            ('A', 'accepted'),
                            ('C', 'commented'),
                        ],
                        max_length=5,
                    ),
                ),
            ],
        ),
    ]