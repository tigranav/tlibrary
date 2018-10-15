# Generated by Django 2.1.2 on 2018-10-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.BigIntegerField(help_text='old id')),
                ('title', models.CharField(help_text='Title of books', max_length=255)),
                ('author', models.CharField(help_text='authors', max_length=255)),
                ('year', models.IntegerField(help_text='year')),
                ('pages', models.IntegerField(help_text='number of pages')),
                ('description', models.CharField(help_text='Description', max_length=4000)),
                ('ISBN', models.CharField(help_text='ISBN', max_length=40)),
                ('inserted', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]