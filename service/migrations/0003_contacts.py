# Generated by Django 4.2.13 on 2024-05-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_attempt_status_alter_mailing_periodicity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Страна')),
                ('identity_nalog_number', models.IntegerField(verbose_name='ИНН')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]