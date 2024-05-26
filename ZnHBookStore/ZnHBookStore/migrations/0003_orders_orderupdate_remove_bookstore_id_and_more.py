# Generated by Django 5.0 on 2024-05-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZnHBookStore', '0002_bookstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookstore',
            name='id',
        ),
        migrations.AddField(
            model_name='bookstore',
            name='book_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]