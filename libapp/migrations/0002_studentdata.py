# Generated by Django 2.2 on 2019-05-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('Branch', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
