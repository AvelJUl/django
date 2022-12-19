from django.contrib import admin, messages
from django.urls import reverse

from .filters import PriceListFilter
from .forms import AdForm
from .models import Ad, Machine, Rubric


from django. db.models import F

def discount(modeladmin, request, queryset):
    f_price = F('price')
    for obj in queryset:
        obj.price = f_price / 2
        obj.save()
    modeladmin.message_user(request, 'Действие выполнено успешно',
                            level=messages.ERROR)
discount.short_description = 'Уменьшить цену вдвое'


class AdInline(admin.TabularInline):
    # fields = ('title', 'content', 'price', )
    model = Ad
    extra = 0
    show_change_link = True
    form = AdForm


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published', )
    # list_editable = ('title', 'content', 'price',)
    list_select_related = ('rubric',)
    # ordering = ('-rubric__name', 'title')
    # sortable_by = ()
    search_fields = ('title', '^content')
    list_filter = (PriceListFilter,)
    empty_value_display = '----'
    form = AdForm
    actions = (discount,)

    fieldsets = (
        (None, {
            'fields': (('title', 'rubric'), 'content'),
            'classes': ('wide',),
        }),
        ('Дополнительные сведения', {
            'fields': ('price',),
            'description': 'Параметры, необязательные для указания.',
        })
    )

    view_on_site = True
    save_as = True
    # save_on_top = False

    # def view_on_site(self, obj):
    #     return reverse('space:detail', kwargs={'id': obj.pk})


class MachineAdmin(admin.ModelAdmin):
    fields = ('spares',)
    filter_horizontal = ('spares',)


admin.site.register(Machine, MachineAdmin)


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    inlines = [AdInline]
