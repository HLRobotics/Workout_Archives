from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
def load_mainpage(request):
    return render(request,'basic_flow\direct.html',{})

def load_subpage(request):
    return render(request,'basic_flow\includelink.html')