from django.shortcuts import render,HttpResponseRedirect
from .models import notes

# Create your views here.
def load_mainpage(request):
    return render(request,'basic_flow\direct.html',{})

def load_subpage(request):
    return render(request,'basic_flow\includelink.html')

def list_all(request):
    all_notes=notes.objects.all()
    return render(request,'basic_flow\display_all.html',{'display':all_notes})