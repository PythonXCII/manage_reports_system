# Generated by Django 3.0.5 on 2020-04-21 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='order.Problem'),
        ),
    ]
