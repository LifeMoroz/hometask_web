from django.contrib import admin

from hometask_web.models import Configuration, PC, Adapter, Connection


class ConfigurationInline(admin.TabularInline):
    model = PC.configuration.through
    extra = 0


class PCAdmin(admin.ModelAdmin):
    inlines = [ConfigurationInline]


admin.site.register(Configuration)
admin.site.register(PC, PCAdmin)
admin.site.register(Adapter)
admin.site.register(Connection)
