from fastai import basic_train, vision
import os

from django.shortcuts import render
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save()
            image_filepath = image_obj.image.path
            model_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'learning_models',
            )
            learn = basic_train.load_learner(model_path)
            image_for_fastai = vision.image.open_image(image_filepath)
            prediction = learn.predict(image_for_fastai)
            predicted_class = prediction[0]
            predicted_class_index = prediction[1].item()
            confidence = prediction[2][predicted_class_index]   
    else:
        form = ImageForm()
        image_obj = None
        predicted_class = None
    context = {
        'form': form,
        'image_obj': image_obj,
        'predicted_class': ' '.join(map(predicted_class.split('_'))),
        'confidence': confidence,
    }
    return render(request, 'wolforhusky_index.html', context)