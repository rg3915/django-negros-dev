from django.contrib import admin

from .models import Customer, Expense

# admin.site.register(Customer)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'customer', 'value', 'payment_date', 'paid')
    search_fields = ('description', 'customer__first_name', 'customer__last_name')  # noqa E501
    list_filter = ('paid',)
    date_hierarchy = 'payment_date'
