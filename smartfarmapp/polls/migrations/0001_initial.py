# Generated by Django 3.1.5 on 2021-01-16 18:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('temp', models.FloatField(default=20.0)),
                ('DIF_AM', models.FloatField(default=0)),
                ('DIF_PM', models.FloatField(default=0)),
                ('D', models.TimeField(default=django.utils.timezone.now)),
                ('N', models.TimeField(default=django.utils.timezone.now)),
                ('HD', models.FloatField(default=0)),
                ('Pband', models.FloatField(default=0)),
                ('CO', models.IntegerField(default=0)),
                ('Light', models.IntegerField(default=0)),
                ('WC', models.IntegerField(default=0)),
                ('StartW', models.IntegerField(default=0)),
                ('EndW', models.IntegerField(default=0)),
                ('WEC', models.FloatField(default=0)),
                ('WRatio', models.IntegerField(default=0)),
                ('WType', models.CharField(choices=[('ds', '다량소회'), ('sd', '소량다회')], max_length=2)),
                ('RHead', models.BooleanField()),
                ('RLeaf', models.BooleanField()),
                ('RFruit', models.BooleanField()),
                ('Overload', models.FloatField(default=0)),
                ('Geodetic', models.CharField(choices=[('fs', '2~3매'), ('sc', '1~2매'), ('no', '무')], max_length=2)),
                ('LAI', models.FloatField(default=0)),
                ('acc_light', models.IntegerField(default=0)),
                ('farm_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('flower_part', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('growpoint_shape', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('leaf_size', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('geodetic_form', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('stem_color', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('flower_size', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('root_form', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('weekly_growth', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('fruit_load', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('number_bloom', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('growpoint_leafcolor', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('flower_shape', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('flower_distance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)])),
                ('farm_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('temp', models.FloatField(default=0)),
                ('CO', models.IntegerField(default=0)),
                ('humidity', models.FloatField(default=0)),
                ('acc_light', models.IntegerField(default=0)),
                ('farm_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.farm')),
            ],
        ),
    ]
