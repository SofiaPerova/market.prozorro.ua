# Generated by Django 2.2.7 on 2020-01-13 15:39

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('criteria', '0004_auto_20191128_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCriteriaRequirementGroupRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('expected_value', models.CharField(max_length=255, null=True)),
                ('min_value', models.CharField(max_length=255, null=True)),
                ('max_value', models.CharField(max_length=255, null=True)),
                ('related_criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criteria.Criteria')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCriteriaRequirementGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255, null=True)),
                ('requirements', models.ManyToManyField(to='profiles.ProfileCriteriaRequirementGroupRequirement')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCriteria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('requirement_groups', models.ManyToManyField(to='profiles.ProfileCriteriaRequirementGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('draft', 'Draft'), ('hidden', 'Hidden')], default='active', max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('classification_id', models.CharField(max_length=10)),
                ('classification_description', models.CharField(max_length=255)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('unit_code', models.CharField(max_length=5)),
                ('unit_name', models.CharField(max_length=50)),
                ('value_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('value_currency', models.CharField(choices=[('active', 'Active'), ('draft', 'Draft'), ('hidden', 'Hidden')], default='U', max_length=3)),
                ('value_value_added_tax_included', models.BooleanField(default=True)),
                ('additional_classification', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None)),
                ('author', models.CharField(max_length=50)),
                ('criteria', models.ManyToManyField(to='profiles.ProfileCriteria')),
                ('images', models.ManyToManyField(to='profiles.ProfileImage')),
            ],
            options={
                'ordering': ('-date_modified',),
            },
        ),
    ]
