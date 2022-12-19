from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Rubric(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    rubric = models.ForeignKey(
        Rubric, verbose_name='Рубрика', on_delete=models.CASCADE,
        related_name='ads'
    )
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    published = models.DateTimeField(
        verbose_name='Опубликовано', auto_now_add=True, db_index=True,
    )

    def __str__(self):
        return f'{self.published} {self.title}'

    def beautiful_title(self):
        return f'СРОЧНО {self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

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


    def get_absolute_url(self):
        return reverse('space:detail', kwargs={'id': self.pk})


class Spare (models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    spares = models.ManyToManyField(Spare)
