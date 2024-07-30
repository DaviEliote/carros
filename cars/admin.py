from django.contrib import admin
from cars.models import Car,brand

# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display= ('model','brand','factory_year','model_year','value')
    search_fields=('brand','model',)

class brandAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields=('nome',)
    

admin.site.register(Car,carAdmin)
admin.site.register(brand,brandAdmin)