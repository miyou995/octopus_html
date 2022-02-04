from django.contrib import admin
from .models import Client, Contact, Category, Invoice, InvoiceItem, Solution, Service, Quote
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')
    readonly_fields = ('date_sent',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40

# class SolutionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id','name')
#     list_per_page = 40

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor')
    list_display_links = ('id','autor')
    list_per_page = 40


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40



# class XYModelForm(forms.ModelForm)
#     class Meta:
#         fields = ('field1, field2', ...)
#         widgets = {
#             'field1': (any widget you like)
#         }

# @admin.register(XYModel)
# class XYModelAdmin(admin.ModelAdmin)
#     form = XYModelForm


def order_detail(obj):
    url = reverse('core:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">Detail</a>')

def order_pdf(obj):
    url = reverse('core:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = 'Invoice'


class InvoiceItemInline(admin.TabularInline):
    model           = InvoiceItem
    raw_id_fields   = ['invoice']

@admin.display()
def total_da(obj):
    return ("%s" % obj.get_total_cost())


@admin.register(Invoice)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'client_phone' ,'client_email' ,'created' ,'updated' ,total_da,'paid', order_detail, order_pdf]
    list_display_links =('id', 'client')
    list_filter = ['paid','updated']
    list_editable = ['paid','client_phone' ,'client_email']
    inlines = [InvoiceItemInline] 
    # actions = [export_to_csv]
    list_per_page = 30






admin.site.register(Quote, QuoteAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Solution, SolutionAdmin)
admin.site.register(Service, ServiceAdmin)
