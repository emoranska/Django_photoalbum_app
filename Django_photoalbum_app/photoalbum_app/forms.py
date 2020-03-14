from django import forms
from django.forms import ModelForm

from photoalbum_app.models import Photo


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['likes_counter']