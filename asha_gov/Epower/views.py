from django.shortcuts import render
from .models import Epower
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    epowers = Epower.objects.all()
    return render(request, 'home.html', {'epowers': epowers})

def epower_detail(request, pk):
    epower = get_object_or_404(Epower, pk=pk)
    return render(request, 'e_detail.html', {'epower': epower})
