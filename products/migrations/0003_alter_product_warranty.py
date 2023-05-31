# Generated by Django 4.2.1 on 2023-05-31 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_brand_alter_product_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="warranty",
            field=models.ForeignKey(
                blank=True,
                default=334,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.warranty",
            ),
            preserve_default=False,
        ),
    ]
