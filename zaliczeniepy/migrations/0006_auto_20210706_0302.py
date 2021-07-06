# Generated by Django 3.2.5 on 2021-07-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaliczeniepy', '0005_auto_20210706_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (0, 'Inne'), (2, 'Komedia'), (4, 'Drama'), (3, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(related_name='aktorzy', to='zaliczeniepy.Film')),
            ],
        ),
    ]