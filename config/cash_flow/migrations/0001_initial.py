# Generated by Django 5.2.1 on 2025-05-26 16:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=255, unique=True, verbose_name='Название статуса')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255, unique=True, verbose_name='Тип операции')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=255, verbose_name='Подкатегория')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='cash_flow.category', verbose_name='Категория')),
            ],
            options={
                'unique_together': {('category', 'subcategory_name')},
            },
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='cash_flow.type', verbose_name='Тип'),
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления записи')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата операции')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Указывается в рублях с копейками', max_digits=12, verbose_name='Сумма')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.category', verbose_name='Категория')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.status', verbose_name='Статус')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.subcategory', verbose_name='Подкатегория')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Движение денежных средств',
                'verbose_name_plural': 'Движения денежных средств',
                'ordering': ['-created_at', '-date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('type', 'category_name')},
        ),
    ]
