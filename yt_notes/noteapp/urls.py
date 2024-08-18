from django.urls import path

from . import views

urlpatterns = [
    path("notes/", views.NoteListCreateAPIView.as_view(), name="notes"),
    path("notes/<int:pk>/",
         views.NoteRetrieveUpdateDestroyAPIView.as_view(), name="note-detail"),
    path("notes-search/", views.search_notes, name='notes-search')
]
