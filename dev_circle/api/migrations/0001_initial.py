# Generated by Django 3.2.15 on 2022-10-07 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('tag_description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('link', models.URLField(null=True)),
                ('code', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('asked_date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='api.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('link', models.URLField(null=True)),
                ('code', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='ans_images')),
                ('answered_date', models.DateTimeField(auto_now_add=True)),
                ('down_vote', models.ManyToManyField(related_name='ans_down', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questions')),
                ('up_vote', models.ManyToManyField(related_name='ans_up', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]