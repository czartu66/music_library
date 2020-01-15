from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm


class IndexView(generic.ListView):
    """Return all of Album objects"""
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    """Make a detailed view"""
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    """Create an Album"""
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    """Update an Album"""
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    """Delete an Album"""
    model = Album
    success_url = reverse_lazy('music:index')

class SongAdd(CreateView):
    """Add a Song"""
    model = Song
    fields = ['album', 'song_title']

class SongUpdate(UpdateView):
    """Update a Song"""
    model = Song
    fields = ['album', 'song_title']

class SongDelete(DeleteView):
    """Delete a Song"""
    model = Song
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    """Create the Registration Form"""
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
