# Generated by Django 4.2.6 on 2024-02-05 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revenues', '0005_alter_recipesubcategoriesrevenues_subcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrevenues',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenues_autor', to=settings.AUTH_USER_MODEL),
        ),
    ]
