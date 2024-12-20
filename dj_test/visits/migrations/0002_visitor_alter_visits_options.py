# Generated by Django 4.2.17 on 2024-12-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='visits',
            options={'verbose_name_plural': 'Visits'},
        ),
    ]
