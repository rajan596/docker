from django.contrib import admin
from index.models import Users , document , documentAdmin , UsersAdmin, Stats,StatsAdmin

# Register your models here.
admin.site.register(Users , UsersAdmin)
admin.site.register(document,documentAdmin)
admin.site.register(Stats, StatsAdmin)
