from django.contrib import admin

from dashboard.models import Area

class AreaModelAdmin(admin.ModelAdmin):
	list_display = ["user","name", "createdtimestamp","modifiedtimestamp"]
	list_display_links = ["modifiedtimestamp"]
	list_editable = ["name"]
	list_filter = ["createdtimestamp","modifiedtimestamp"]
	class Meta:
		model = Area

admin.site.register(Area,AreaModelAdmin)