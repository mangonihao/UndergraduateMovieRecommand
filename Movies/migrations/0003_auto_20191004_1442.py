# Generated by Django 2.2.3 on 2019-10-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_movie_movie_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_cover',
            field=models.ImageField(null=True, upload_to='MovieCover/%Y/%m/%d', verbose_name='电影封面图片路径'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_intro',
            field=models.CharField(max_length=512, null=True, verbose_name='剧情简介'),
        ),
    ]
