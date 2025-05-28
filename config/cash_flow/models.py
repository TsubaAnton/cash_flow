from django.utils import timezone
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Status(models.Model):
    status_name = models.CharField(max_length=255, unique=True, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    type_name = models.CharField(max_length=255, unique=True, verbose_name='Тип операции')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories', verbose_name='Тип')
    category_name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ('type', 'category_name')


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory', verbose_name='Категория')
    subcategory_name = models.CharField(max_length=255, verbose_name='Подкатегория')

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        unique_together = ('category', 'subcategory_name')


class CashFlow(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления записи')
    date = models.DateField(default=timezone.now, verbose_name='Дата операции')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name='Подкатегория')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма', help_text='Указывается в рублях с копейками')
    description = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'Дата создания: {self.created_at}, Тип: {self.type}, Сумма: {self.amount} руб.'

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'
        ordering = ['-created_at', '-date']

