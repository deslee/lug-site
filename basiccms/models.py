from django.db import models

# Create your models here.
class SidebarElement(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	content = models.TextField()

class Sidebar(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	elements = models.ManyToManyField(SidebarElement)

class Page(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=20)
	sidebar = models.ForeignKey(Sidebar, null=True, blank=True)

class Article(models.Model):
	def __str__(self):
		return self.title
	page = models.ForeignKey(Page)
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')
	sortorder = models.IntegerField(null=True, blank=True)