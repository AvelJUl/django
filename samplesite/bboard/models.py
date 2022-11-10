from django.core.exceptions import ValidationError
from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    rubric = models.ForeignKey(
        Rubric, on_delete=models.PROTECT, blank=True, null=True,
        related_name='ads'
    )
    title = models.CharField(max_length=50)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.published} {self.title}'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара'
            )
        if self.price and self.price < 0:
            errors['price'] = ValidationError(
                'Укажите неотрицательное значение цены'
            )
        if errors:
            raise ValidationError(errors)

    # def save(
    #     self, force_insert=False, force_update=False,
    #         using=None, update_fields=None
    # ):
    #     self.clean()
    #     super().save(force_insert, force_update, using, update_fields)


class Spare (models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    spares = models.ManyToManyField(Spare)