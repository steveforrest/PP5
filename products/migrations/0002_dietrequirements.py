# Generated by Django 3.2 on 2022-09-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergens', models.IntegerField(choices=[(1, 'Gluten'), (2, 'Lactose'), (3, 'Eggs'), (4, 'Peanuts'), (5, 'Fish'), (6, 'Shellfish'), (7, 'Kosha'), (8, 'Halal')])),
                ('dietRequirement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='products.product')),
            ],
        ),
    ]
