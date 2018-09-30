# Generated by Django 2.1.1 on 2018-09-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(max_length=6)),
                ('cn', models.CharField(max_length=30)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('andrewID', models.CharField(max_length=10)),
                ('fn', models.CharField(max_length=10)),
                ('ln', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='Rego.Student'),
        ),
    ]
