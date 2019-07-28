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
            prediction = load_and_predict(image_filepath, model_path)
            predicted_class = str(prediction[0]).replace('_', ' ')
            predicted_class_index = prediction[1].item()
            confidence = int(100*prediction[2][predicted_class_index].item())  
    else:
        form = ImageForm()
        image_obj = None
        predicted_class = None
        confidence = None
    context = {
        'form': form,
        'image_obj': image_obj,
        'predicted_class': predicted_class,
        'confidence': confidence,
    }
    return render(request, 'wolforhusky_index.html', context)

def load_and_predict(image_filepath, model_path):
    learn = basic_train.load_learner(model_path)
    image_for_fastai = vision.image.open_image(image_filepath)
    return learn.predict(image_for_fastai, model_path)