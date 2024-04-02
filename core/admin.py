from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)

class Imginlines(admin.TabularInline):
    model = ProjectImage

@admin.register(Projects)
class product(admin.ModelAdmin):
    inlines = [ Imginlines, ]
    prepopulated_fields = {'slug': ('title',)}
