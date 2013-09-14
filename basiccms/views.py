from django.http import HttpResponse 
from basiccms.models import Page
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'basiccms/basictemplate.html', {
    	'title' : 'UTDLUG',
    	'sidebar': {'elements': [{'title': "hello", 'content': "hello world"}]},
    	'articles': {'title': "hello", 'content': "hello world"}
    	});

def page(request, slug):
	page = get_object_or_404(Page, slug=slug)
	model = {
	'title': page.title,
	'articles': page.article_set.all(),
	'sidebar': {
		'title': page.sidebar.title,
		'elements': page.sidebar.elements.all(),
	},
	}
	return render(request, 'basiccms/basictemplate.html', model)