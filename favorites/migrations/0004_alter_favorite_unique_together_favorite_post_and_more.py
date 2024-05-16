# Generated by Django 4.2 on 2024-05-14 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0003_alter_favorite_unique_together_remove_favorite_post'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='favorite',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='posts.post'),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('owner', 'post')},
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='detectorist',
        ),
    ]