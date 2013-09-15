from django.http import HttpResponse 
from basiccms.models import Page
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
	page = get_object_or_404(Page, slug='index')
	return render(request, 'basiccms/basictemplate.html', model_from_page(page))

def page(request, slug):
	if slug == 'index':
		return redirect(index)
	page = get_object_or_404(Page, slug=slug)
	return render(request, 'basiccms/basictemplate.html', model_from_page(page))

def model_from_page(page):
	model = {
		'title': page.title,
		'articles': page.article_set.order_by('sortorder', '-pub_date').all(),
	}
	if (page.sidebar):
		model['sidebar'] =  {
			'title': page.sidebar.title,
			'elements': page.sidebar.elements.all(),
		}
	return model	
