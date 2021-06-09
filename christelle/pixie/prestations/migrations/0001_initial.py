# Generated by Django 3.2.4 on 2021-06-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=False)),
                ('image', models.FileField(upload_to='image_Prestations')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.IntegerField(default=True)),
                ('description', models.TextField()),
                ('chare', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_fichier', to='prestations.categorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'produits',
            },
        ),
    ]