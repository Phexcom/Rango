from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['category']}),
        ('Page Details', {'fields': ['title', 'url']})

    ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category)
admin.site.register(Page, PageAdmin)


