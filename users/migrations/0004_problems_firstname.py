# Generated by Django 5.0.3 on 2024-03-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_comments_product_problems_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='firstname',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]