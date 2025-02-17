from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

def item_create(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        description = request.POST.get('description')
        item = Item.objects.create(name=name, description=description)
        return redirect('item_create')
    
    return render(request, 'test_app/item_form.html')
