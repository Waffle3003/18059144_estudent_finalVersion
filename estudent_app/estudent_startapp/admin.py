from django.contrib import admin
from .models import Budget, Need, Want, Saving, Goal

# Register your models here.
admin.site.register(Budget)
admin.site.register(Need)
admin.site.register(Want)
admin.site.register(Saving)
admin.site.register(Goal)