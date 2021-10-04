from django.contrib import admin
from .models import ContactForm, Category, Solution, Service, Quote
from django.contrib.auth.models import Group, User
from django.utils.html import format_html

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')


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


admin.site.register(Quote, QuoteAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Solution, SolutionAdmin)
admin.site.register(Service, ServiceAdmin)