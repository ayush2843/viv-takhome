from django.urls import path
from .views import LoadJsonDataView, PlaylistDataListView, PlaylistDataDetailView

urlpatterns = [
    path(
        "v1/preprocess/load-playlist-data",
        LoadJsonDataView.as_view(),
        name="load_playlist_data",
    ),
    path(
        "v1/api/playlist-data",
        PlaylistDataListView.as_view(),
        name="playlist_data_list",
    ),
    path(
        "v1/api/playlist-data/field",
        PlaylistDataDetailView.as_view(),
        name="playlist_data_list",
    ),
]
