# Generated by Django 3.2 on 2021-04-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('survey_idx', models.IntegerField()),
                ('ans', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='survey',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(null=True)),
                ('ans1', models.TextField(null=True)),
                ('ans2', models.TextField(null=True)),
                ('ans3', models.TextField(null=True)),
                ('ans4', models.TextField(null=True)),
                ('status', models.CharField(default='y', max_length=1)),
            ],
            options={
                'verbose_name': '질문',
                'verbose_name_plural': '질문들',
                'db_table': 'survey_table',
            },
        ),
    ]
