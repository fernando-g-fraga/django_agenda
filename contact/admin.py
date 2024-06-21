from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    ...