from django.db import models

# Create your models here.
class Page(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=20)

class Article(models.Model):
	def __str__(self):
		return self.title
	page = models.ForeignKey(Page)
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')

class Sidebar(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	page = models.ForeignKey(Page)

class SidebarElement(models.Model):
	def __str__(self):
		return self.title
	sidebar = models.ForeignKey(Sidebar)
	title = models.CharField(max_length=200)
	content = models.TextField()