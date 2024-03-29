# Generated by Django 4.1 on 2023-01-15 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_book_id_alter_book_member_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='member_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='management.member'),
        ),
    ]
