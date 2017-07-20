from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item




def index1(request):
    all_items=Item.objects.all()
    context={'all_items':all_items}
    return render(request,'category/index1.html',context)



def detail(request,item_id):
    try:
        item= Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item DoesNot Exists")
    return render(request,'category/detail.html',{'item':item})

