# Generated by Django 2.2 on 2019-05-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=6, max_digits=6)),
                ('status', models.CharField(choices=[('Available', 'Item ready purchase'), ('Sold', 'Item sold'), ('Restocking', 'Restocking in few days')], default='Available', max_length=30)),
                ('issues', models.CharField(default='No issues', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('Available', 'Item ready purchase'), ('Sold', 'Item sold'), ('Restocking', 'Restocking in few days')], default='Available', max_length=30)),
                ('issues', models.CharField(default='No issues', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('Available', 'Item ready purchase'), ('Sold', 'Item sold'), ('Restocking', 'Restocking in few days')], default='Available', max_length=30)),
                ('issues', models.CharField(default='No issues', max_length=30)),
            ],
        ),
    ]