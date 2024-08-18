from django.urls import path

from . import views

urlpatterns = [
    path("notes/", views.NoteListCreateAPIView.as_view(), name="notes"),
    path("notes/<str:slug>/",
         views.NoteRetrieveUpdateDestroyAPIView.as_view(), name="note-detail"),
    path("notes-search/", views.SearchNotesAPIView.as_view(), name='notes-search')
]
