from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from photoalbum_app.forms import AddPhotoForm
from photoalbum_app.models import Photo


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class AllPhotosView(View):
    def get(self, request):
        form = AddPhotoForm()
        photos = Photo.objects.all()
        return render(request, 'all-photos.html', {"form": form, "photos": photos})

    def post(self, request):
        form = AddPhotoForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['app_user']
            return HttpResponseRedirect(f'/photoalbum/{user}')


class UserPhotosView(View):
    def get(self, request, user):
        app_user = User.objects.get(username=user)
        photos = Photo.objects.filter(app_user=app_user)
        return render(request, 'user-photos.html', {"photos": photos})


class PhotoDetailsView(View):
    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        return render(request, 'photo-details.html', {"photo": photo})