# Generated by Django 4.2.7 on 2024-05-13 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_provider_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='products',
        ),
        migrations.AddField(
            model_name='branch',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.product'),
            preserve_default=False,
        ),
    ]
