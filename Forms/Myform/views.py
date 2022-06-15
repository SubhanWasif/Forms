from django.shortcuts import render
from .forms import formsForm



def index(request):
    if request.method == "POST":
        form = formsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HTML/Submitted.html',context={})

            
    else:
        form = formsForm()
    context = {'form':form}

    return render(request, 'HTML/form.html',context)
    