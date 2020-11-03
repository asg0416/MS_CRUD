# Generated by Django 3.1.2 on 2020-10-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('desc', models.TextField(blank=True, verbose_name='본문')),
                ('pic', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
            ],
        ),
    ]
