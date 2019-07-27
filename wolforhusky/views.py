from django.shortcuts import render
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # img = request.FILES['image']
            # handle_file(request.FILES['file'])
    else:
        form = ImageForm()
    context = {
        'form': form,
        # 'img': img,
    }
    return render(request, 'wolforhusky_index.html', context)