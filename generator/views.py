from django.shortcuts import render, redirect

from generator.forms import WebPageForm
from generator.models import WebPage


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = WebPageForm()
    else:
        form = WebPageForm(request.POST)
        if form.is_valid():
            webpage = form.save()
            return redirect('view_page', pk=webpage.pk)
    return render(request, 'generator/index.html', {'form': form})


def view_page(request, pk):
    webpage = WebPage.objects.get(pk=pk)
    return render(request, 'generator/view_page.html', {'webpage': webpage})
