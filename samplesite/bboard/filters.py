from django.contrib.admin import SimpleListFilter


class PriceListFilter(SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (('low', 'Низкая цена'), ('medium', 'Средняя цена'), ('high', 'Высокая цена'),)

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=500)
        elif self.value() == 'medium':
            return queryset.filter(price__gte=500, price__lte=5000)
        elif self.value() == 'high':
            return queryset.filter(price__gt=5000)