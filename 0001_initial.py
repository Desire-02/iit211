# Generated by Django 5.1.3 on 2025-02-15 09:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('yas', 'Yas'), ('flooz', 'Flooz')], max_length=10)),
                ('type_transaction', models.CharField(choices=[('depot', 'Dépôt'), ('retrait', 'Retrait')], max_length=8)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode_paiement', models.CharField(max_length=10)),
                ('date_paiement', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiements', to='BoutikApp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.PositiveIntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='BoutikApp.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='DetailVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoutikApp.produit')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePanier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='BoutikApp.panier')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoutikApp.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventes', to='BoutikApp.client')),
                ('produits', models.ManyToManyField(through='BoutikApp.DetailVente', to='BoutikApp.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Recu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateField(auto_now_add=True)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BoutikApp.vente')),
            ],
        ),
        migrations.AddField(
            model_name='detailvente',
            name='vente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoutikApp.vente'),
        ),
    ]
