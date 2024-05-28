# Generated by Django 5.0 on 2024-05-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZnHBookStore', '0005_bookstore_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
