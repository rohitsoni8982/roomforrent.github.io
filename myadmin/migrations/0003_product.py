# Generated by Django 4.1.2 on 2023-04-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myadmin", "0002_subcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("pid", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("catname", models.CharField(max_length=50)),
                ("subcatname", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
                ("locality", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("piconname", models.CharField(max_length=100)),
                ("info", models.CharField(max_length=50)),
            ],
        ),
    ]
