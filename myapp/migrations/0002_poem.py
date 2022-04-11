# Generated by Django 3.2.8 on 2022-04-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=100)),
                ('lines', models.IntegerField()),
                ('stanzas', models.IntegerField()),
            ],
        ),
    ]
