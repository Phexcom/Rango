from django.contrib import admin
from rango.models import Category, Page

<<<<<<< HEAD

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['category']}),
        ('Page Details', {'fields': ['title', 'url']})

    ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category)
admin.site.register(Page, PageAdmin)

=======
admin.site.register(Category)
admin.site.register(Page)
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
