from django.contrib import admin
from .models import Pick,Player,League

# Register your models here.
admin.site.register(Pick)
admin.site.register(League)
admin.site.register(Player)