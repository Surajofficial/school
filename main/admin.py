from django.contrib import admin
from .models import School, Parent, Payment, Kid


@admin.action(description='Generate payment link')
def generate_payment_link(modeladmin, request, queryset):
    for parent in queryset:
        parent.generate_payment_link()
    modeladmin.message_user(request, "Payment links generated successfully.")


class ParentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_mobile1',
                    'user_email_id', 'payment_link', 'created_date']
    actions = [generate_payment_link]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['parent', 'amount',
                    'status', 'created_date']


admin.site.register(School)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Payment)
admin.site.register(Kid)
