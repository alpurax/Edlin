from django.contrib import admin
from .models import Post

class PAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','published')
    list_display_links = ('title','content')
    search_fields = ('title','content')

admin.site.register(Post,PAdmin)

