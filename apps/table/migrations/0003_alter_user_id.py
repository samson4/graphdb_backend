# Generated by Django 4.2.6 on 2024-08-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("table", "0002_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
