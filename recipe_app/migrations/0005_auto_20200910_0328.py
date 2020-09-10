# Generated by Django 3.1.1 on 2020-09-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0004_recipe_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorite',
        ),
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to='recipe_app.Recipe'),
        ),
    ]