from django.shortcuts import render
from .forms import UploadImageForm


def index(request):
    form = UploadImageForm()
    context = {
        'form': form
    }
    return render(request, 'wolforhusky_index.html', context)