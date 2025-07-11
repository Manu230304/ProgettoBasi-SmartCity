# Generated by Django 5.2.1 on 2025-06-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCity', '0022_alter_urbanista_qualifica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urbanista',
            name='qualifica',
            field=models.CharField(choices=[('laurea_triennale_urbanistica', 'Laurea triennale in Urbanistica'), ('laurea_magistrale_pianificazione', 'Laurea magistrale in Pianificazione Territoriale'), ('master_urbanistica', 'Master in Urbanistica e Pianificazione Urbana'), ('dottorato_scienze_urbanistiche', 'Dottorato in Scienze Urbanistiche'), ('abilitazione_professionale', 'Abilitazione professionale all’esercizio della professione di Urbanista'), ('certificazione_gis', 'Certificazione in GIS (Geographic Information Systems)'), ('corso_rigenerazione', 'Corso di specializzazione in Rigenerazione Urbana'), ('esperto_sostenibilita', 'Esperto in Sostenibilità e Pianificazione Ambientale'), ('esperto_mobilita', 'Esperto in Mobilità Urbana e Trasporti'), ('certificazione_pmp', 'Certificazione in Project Management (es. PMP)'), ('esperto_politiche_abitative', 'Esperto in Politiche Abitative e Sociali'), ('esperto_normativa', 'Esperto in Normativa Urbanistica e Edilizia')], max_length=120),
        ),
    ]
