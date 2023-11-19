from django.contrib import admin
from .models import events, slider
from .models import category
# Register your models here.

@admin.register(events)
class eventsAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","date","slug","category_list","image",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("isActive","date",)
    search_fields = ("title","description",)

    def category_list(self,category_l):
        html = ""
        for category in category_l.categories.all():
            html += category.name + " "
            return html



@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
   list_display = ("name","slug","events_count",)
   list_display_links = ("name", "slug",)
   prepopulated_fields = {"slug" : ("name",),}

   def events_count(self,events_obj):
       return events_obj.events_set.count()

admin.site.register(slider)

