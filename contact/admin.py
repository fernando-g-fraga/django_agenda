from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone',)
    ordering = 'id',
    search_fields = ('first_name','id','last_name',)
    list_per_page = 10
    list_max_show_all = 50
    # list_editable = 'first_name','last_name',

