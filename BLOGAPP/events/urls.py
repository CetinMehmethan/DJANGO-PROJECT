from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name="index"),
path('search',views.search,name = "search"),
path('create-events',views.create_events,name = "create_events"),
path('events-list',views.events_list,name = "events_list"),
path('events-edit/<int:id>',views.events_edit,name="events_edit"),
path('events-delete/<int:id>',views.events_delete,name="events_delete"),
path('upload-image',views.upload,name="upload_image"),
path('<slug:slug>',views.details,name = "events_details"),
path('category/<slug:slug>',views.eventByToCategory,name = "event_by_category"),

]
