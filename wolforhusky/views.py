from django.shortcuts import render
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
    else:
        form = ImageForm()
        image = None
    context = {
        'form': form,
        'image': image,
    }
    return render(request, 'wolforhusky_index.html', context)