from fastai import basic_train, vision
import os

from django.shortcuts import render
from .forms import ImageForm

def index(request):
    context = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save()
            model_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'learning_models',
            )
            context['predicted_class'], context['confidence'] = get_prediction_data(
                image_obj.image.path, model_path
            )
            context['image_obj'] = image_obj
    else:
        form = ImageForm()
    context['form'] = form

    return render(request, 'wolforhusky_index.html', context)

def get_prediction_data(image_filepath, model_path):
    learn = basic_train.load_learner(model_path)
    image_for_fastai = vision.image.open_image(image_filepath)
    prediction = learn.predict(image_for_fastai)
    predicted_class = str(prediction[0]).replace('_', ' ')
    predicted_class_index = prediction[1].item()
    confidence = int(100*prediction[2][predicted_class_index].item())
    return predicted_class, confidence