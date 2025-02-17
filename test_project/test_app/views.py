from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

# Create your views here.

def item_create(request):
    
    # POST 요청이면 사용자의 데이터를 받아 Item 모델에 저장장
    if request.method == "POST" :
        name = request.POST.get('name')
        description = request.POST.get('description')
        item = Item.objects.create(name=name, description=description)
        return redirect('item_create')
    
    # GET 요청이면 폼을 보여줌
    return render(request, 'item_form.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items':items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item':item})

