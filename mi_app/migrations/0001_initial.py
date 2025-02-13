# Generated by Django 5.0.7 on 2024-07-22 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Lama",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tipo", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Panel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tipo", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("material", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PVC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=100)),
                (
                    "precio_unitario",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vidrio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tipo", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("espesor", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Presupuesto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField(auto_now_add=True)),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("numero", models.PositiveIntegerField(unique=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mi_app.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Puerta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tipo", models.CharField(max_length=100)),
                (
                    "revestimiento_lama",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.lama",
                    ),
                ),
                (
                    "revestimiento_panel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.panel",
                    ),
                ),
                (
                    "revestimiento_vidrio",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.vidrio",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ventana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tipo", models.CharField(max_length=100)),
                (
                    "revestimiento_lama",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.lama",
                    ),
                ),
                (
                    "revestimiento_panel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.panel",
                    ),
                ),
                (
                    "revestimiento_vidrio",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.vidrio",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DetallePresupuesto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.PositiveIntegerField()),
                (
                    "presupuesto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detalles",
                        to="mi_app.presupuesto",
                    ),
                ),
                (
                    "puerta",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.puerta",
                    ),
                ),
                (
                    "ventana",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mi_app.ventana",
                    ),
                ),
            ],
        ),
    ]
