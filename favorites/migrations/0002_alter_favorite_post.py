# Generated by Django 3.2.25 on 2024-04-26 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='posts.post'),
        ),
    ]
