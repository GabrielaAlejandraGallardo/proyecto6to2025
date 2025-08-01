# Generated by Django 4.2 on 2025-06-27 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='idCategoria')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('iddescripciondeporte', models.AutoField(primary_key=True, serialize=False, verbose_name='iddescripciondeporte')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='DeporteD',
            fields=[
                ('idDeporte', models.AutoField(db_column='idDeporte', primary_key=True, serialize=False)),
                ('horario', models.DateTimeField(verbose_name='horario')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deportes.categoria', verbose_name='idCategoria')),
                ('iddescripciondeporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deportes.d', verbose_name='iddescripciondeporte')),
            ],
        ),
    ]
