# Generated by Django 2.0 on 2020-06-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_form', '0002_auto_20200601_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='sie_utilisateur',
            name='UTI_NUMBER',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
