from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Service)
admin.site.register(Blog)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description')
    list_filter = ('category', )
    list_editable = ('category', )


