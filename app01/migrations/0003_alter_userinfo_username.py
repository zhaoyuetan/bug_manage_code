# Generated by Django 4.1.7 on 2023-04-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_alter_userinfo_email_alter_userinfo_mobile_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="username",
            field=models.CharField(db_index=True, max_length=32, verbose_name="用户名"),
        ),
    ]
