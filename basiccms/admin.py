from django.contrib import admin
from basiccms.models import Page, Article, Sidebar, SidebarElement
class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1

class SidebarElementInline(admin.TabularInline):
	model = Sidebar.elements.through

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,		{'fields': ['title']}),
        (None,		{'fields': ['slug']}),
        (None,		{'fields': ['sidebar']}),
    ]
    inlines = [ArticleInline]

class SidebarAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': ['title']}),
	]
	inlines = [SidebarElementInline]

admin.site.register(Page, PageAdmin)
admin.site.register(Article)
admin.site.register(Sidebar, SidebarAdmin)
admin.site.register(SidebarElement)