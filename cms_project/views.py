from django.shortcuts import render
from cms_app.models import ContentItem

def home(request):
    content_items = ContentItem.objects.all()
    return render(request, 'home.html', {'content_items': content_items})