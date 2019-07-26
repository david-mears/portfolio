from django import forms

class UploadImageForm(forms.Form):
    image_to_classify = forms.ImageField()