# Generated by Django 2.2.3 on 2019-09-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('movie_id', models.AutoField(primary_key=True, serialize=False, verbose_name='电影id')),
                ('movie_name', models.CharField(max_length=100, unique=True, verbose_name='电影片名')),
                ('movie_length', models.IntegerField(default=0, verbose_name='电影片长')),
                ('movie_releaseTime', models.DateField(verbose_name='上映时间')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
