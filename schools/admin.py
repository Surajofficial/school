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


class KidAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'name',
                    'school_name', 'roll_number', 'monthly_fees']

    def parent_name(self, obj):
        return obj.parent.user_name
    parent_name.short_description = 'Parent Name'

    def school_name(self, obj):
        return obj.school.school_name
    parent_name.short_description = 'Parent Name'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'parent_mobile', 'school_name',
                    'payment_status', 'paid_amount', 'payment_date', 'transaction_id')
    readonly_fields = ('parent_name', 'parent_mobile', 'school_name')

    def parent_name(self, obj):
        return obj.parent.user_name
    parent_name.short_description = 'Parent Name'

    def parent_mobile(self, obj):
        return obj.parent.user_mobile1
    parent_mobile.short_description = 'Parent Mobile'

    def school_name(self, obj):
        return obj.school.school_name
    school_name.short_description = 'School Name'


admin.site.register(Payment, PaymentAdmin)

admin.site.register(School)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Kid, KidAdmin)
