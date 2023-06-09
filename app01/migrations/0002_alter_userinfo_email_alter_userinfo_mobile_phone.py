# Generated by Django 4.1.7 on 2023-04-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="email",
            field=models.EmailField(max_length=32, verbose_name="邮箱"),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="mobile_phone",
            field=models.CharField(max_length=32, verbose_name="手机号"),
        ),
    ]
