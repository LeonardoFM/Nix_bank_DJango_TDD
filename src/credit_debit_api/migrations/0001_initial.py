# Generated by Django 3.1.2 on 2020-10-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('balance', models.IntegerField()),
                ('debit', models.IntegerField(blank=True, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
    ]
