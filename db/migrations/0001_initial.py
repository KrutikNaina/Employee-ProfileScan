# Generated by Django 5.0.6 on 2025-03-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=30)),
                ('ename', models.CharField(max_length=30)),
                ('eadd', models.CharField(max_length=30)),
                ('esal', models.IntegerField()),
                ('ecity', models.CharField(max_length=30)),
                ('eimg', models.FileField(default=None, max_length=250, null=True, upload_to='upload/')),
            ],
        ),
    ]
