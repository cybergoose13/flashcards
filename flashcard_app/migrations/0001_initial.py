# Generated by Django 3.1.4 on 2020-12-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=32)),
                ('question', models.CharField(max_length=128)),
                ('answer', models.CharField(max_length=64)),
                ('wrong_one', models.CharField(max_length=64)),
                ('wrong_two', models.CharField(max_length=64)),
                ('wrong_three', models.CharField(max_length=64)),
                ('created_by', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
