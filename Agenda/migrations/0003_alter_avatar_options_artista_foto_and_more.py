# Generated by Django 4.1.7 on 2023-03-07 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Agenda', '0002_alter_vidanocturna_options_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avatar',
            options={'verbose_name_plural': 'Avatares'},
        ),
        migrations.AddField(
            model_name='artista',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
