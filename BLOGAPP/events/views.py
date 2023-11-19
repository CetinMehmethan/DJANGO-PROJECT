import os.path
import random
from PIL import Image
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventCreateForm, EventEditForm, UploadForm
from .models import category, UploadModel
from .models import events , slider
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.messages import add_message

def index(request):
    events1 = events.objects.filter(isActive = True,isHome = True).order_by('-date')
    kategoriler= category.objects.all()
    sliders = slider.objects.filter(is_active=True)

    return render(request, "index_events.html",{
        'categories': kategoriler,
        'events': events1,
        'sliders':sliders
    })


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
     q = request.GET["q"]
     events_by = events.objects.filter(isActive=True,title__contains=q)
     events_by.order_by("date")
     kategoriler = category.objects.all()
    else:
     return redirect("/events")

    return render(request, "_search.html", {
        'categories': kategoriler,
        'events': events_by,

    })


def isAdmin(user):
    return user.is_superuser
@user_passes_test(isAdmin)
def create_events(request):

    if request.method == "POST":
        form = EventCreateForm(request.POST,request.FILES)

        if form.is_valid():
         form.save()
         return render(request, template_name="success.html")
    else:
     form = EventCreateForm()
     return render(request,"create-events.html",{"form":form})


def events_list(request):
    events_by = events.objects.all()
    return render(request, "events-list.html", {
        'events': events_by})
def events_edit(request,id):
    events_et= get_object_or_404(events,id= id)
    if request.method == "POST":
        form = EventEditForm(request.POST,request.FILES,instance=events_et)
        form.save()
        return redirect("events_list")
    else:
     form = EventEditForm(instance=events_et)
    return render(request,"events-edit.html",{"form":form})

def events_delete(request,id):
    events_dt = get_object_or_404(events,id=id)
    if request.method == "POST":
        events_dt = EventEditForm(request.POST,request.FILES,instance=events_dt)
        events.objects.filter(id=id).delete()
        return redirect("events_list")
    return render(request, "events-delete.html", {"event":events_dt})
def details(request,slug):
    #event_ds = events.objects.get(pk = events_id)
    event_ds = get_object_or_404(events,slug =slug)
    context = {
        "event1" :event_ds
    }
    return render(request,"details.html",context)

def upload(request):
    if request.method == "POST":
      form = UploadForm(request.POST,request.FILES)

      if form.is_valid():
         model = UploadModel(image=request.FILES["image"])
         model.save()
      return render(request,template_name="success.html")
    else:
        form = UploadForm()
    return render(request,"upload-image.html",{"form":form})

"""def handle_uploaded_files(file):
    number = random.randint(11111,99999)
    filename ,file_extention =os.path.splitext(file.name)
    name = filename +"_"+str(number)+file_extention
    with open("temp/"+name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)"""



def eventByToCategory(request, slug):
    events_by = events.objects.filter(categories__slug=slug,isActive = True).order_by('-date')
    events_by.order_by("date")
    kategoriler = category.objects.all()

    paginator = Paginator(events_by,3)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    print(page_obj.paginator.count)
    print(page_obj.paginator.num_pages)

    return render(request,"_list.html",{
      'categories': kategoriler,
      'page_obj': page_obj,
      's_category': slug,
    })




