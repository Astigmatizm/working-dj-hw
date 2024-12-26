from django.contrib import admin
from .models import Product

# name = admin1
# email = admin@dj.kz
# password = 12345


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'price', 'created_at', 'updated_at')  # Показать имя, цену, дату создания и обновления
    search_fields = ('name', 'description')  # Возможность поиска по имени и описанию товара
    list_filter = ('created_at', 'price')  # Фильтрация по дате создания и цене
    list_editable = ('price',)  # Возможность редактировать цену товара в списке
    ordering = ('-created_at',)  # Сортировка по дате создания



