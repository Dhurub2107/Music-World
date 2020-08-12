from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Album,Song
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate
from .form import LoginForm,SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views.generic.edit import FormView
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

''' view for home in fun
def home(request):
    a=Album.objects.all()
    return render(request,"music/home.html",{'album':a})
    '''
class Home(ListView):
    template_name="music/home.html"
    context_object_name = 'album'
    def get_queryset(self):
       return Album.objects.all()
class Songview(DetailView):
    template_name = "music/song.html"
    model=Album
    context_object_name = "album"

class Login(CreateView):
    from_class = LoginForm
    template_name = "music/login.html"
    def get(self, request, *args, **kwargs):
        myform=LoginForm()
        return render(request,self.template_name,{"form":myform})
    def post(self, request, *args, **kwargs):
        myform = LoginForm(request.POST)
        if myform.is_valid():
            usern=myform.cleaned_data.get("username")
            passw=myform.cleaned_data.get("password")
            val=authenticate(username=usern,password=passw)

            if val is not None:
                request.session["loginuser"]=usern
                #return messages.info(request,"Login Sucessfull Welcome"+usern)
                return redirect("/gaana/")
        return  render(request,"music/login.html",{"form":myform})

def logout(request):
    #v=tkMessageBox.askokcancel("Music World","Do you want to logout")
    #if v==True:
        return redirect("/login/")

class Register(FormView):
    from_class=SignUpForm
    template_name ="music/signup.html"
    def get(self,request,*args,**kwargs):
        myform=SignUpForm()
        return render(request,self.template_name,{"form":myform})
    def post(self,request,*args,**kwargs):
        myform=SignUpForm(request.POST)
        if myform.is_valid():
            usern = myform.cleaned_data.get("username")
            passw1 = myform.cleaned_data.get("password1")
            val = authenticate(username=usern, password=passw1)
            if val is not None:
                        return redirect("/login/")

        return render(request, "music/signup.html", {"form": myform})
class AddAlbum(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name=reverse_lazy("music:album")
    model=Album
    fields = ['title','artist','genre','a_logo']
class AlbumUpdate(UpdateView):
    model=Album
    fields = ['title','artist','genre','a_logo']
class AlbumDelete(DeleteView):
    model=Album
    template_name ='music/Album_delete.html'
    context_object_name = "album"
    success_url = reverse_lazy("music:album")
class AddSong(CreateView):
    model=Song
    template_name ='music/Add_Song.html'
    fields = ['stitle', 'sartist', 'aid','filetype','file']
class Play(DetailView):
    template_name = "music/play.html"
    model=Song
    context_object_name = "song"
class SongDelete(DeleteView):
    model=Song
    template_name ='music/Song_delete.html'
    context_object_name = "song"
    success_url = reverse_lazy("music:album")

