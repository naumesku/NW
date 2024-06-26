# Generated by Django 4.2.7 on 2024-05-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_branch_time_alter_product_data_release_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='старна'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='house_nomber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='номер дома'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='register_form',
            field=models.CharField(choices=[('factory', 'завод'), ('ip', 'индивидуальный предприниматель'), ('rs', 'розничеая сеть')], verbose_name='форма регистрации'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='улица'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='town',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='город'),
        ),
    ]
