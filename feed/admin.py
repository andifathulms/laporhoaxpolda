from django.contrib import admin

from .models import Feed, NewsCategory

class FeedAdmin(admin.ModelAdmin):
	list_display = ('title','img_b64')

admin.site.register(Feed)
admin.site.register(NewsCategory)
