from django.contrib import admin
from basiccms.models import Page, Article, Sidebar, SidebarElement
class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,		{'fields': ['title']}),
        (None,		{'fields': ['slug']}),
    ]

    inlines = [ArticleInline]

admin.site.register(Page, PageAdmin)
admin.site.register(Article)
