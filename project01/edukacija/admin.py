from django.contrib import admin

# Register your models here.
from .models import Edukacija

class EdukacijaAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug']
	class Meta:
		model = Edukacija

admin.site.register(Edukacija,EdukacijaAdmin)