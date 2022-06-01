# Generated by Django 4.0 on 2022-05-31 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128, verbose_name='Мембер')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала')),
                ('stop_time', models.DateTimeField(verbose_name='Время окончания')),
                ('permanent', models.BooleanField(default=False, verbose_name='Бан перманентно')),
            ],
            options={
                'verbose_name': 'Блокировка',
                'verbose_name_plural': 'Блокировки',
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Тема')),
                ('description', models.TextField(max_length=255, verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Справка',
                'verbose_name_plural': 'Справки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128, unique=True, verbose_name='id')),
                ('username', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ник')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('role', models.CharField(blank=True, max_length=128, null=True, verbose_name='Роль в канале')),
                ('violation', models.IntegerField(default=0, verbose_name='Количество нарушений')),
            ],
            options={
                'verbose_name': 'Мембер',
                'verbose_name_plural': 'Мемберы',
                'ordering': ['user_id', 'username'],
            },
        ),
    ]
