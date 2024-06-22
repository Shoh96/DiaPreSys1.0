# Generated by Django 4.1 on 2024-06-22 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('skin_thickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.patient')),
            ],
        ),
    ]