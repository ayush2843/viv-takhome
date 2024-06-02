# myapp/views.py
import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializer import PlaylistDataSerializer
from .models import PlaylistData


class LoadJsonDataView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        file_path = os.path.join(os.path.dirname(__file__), "data", "playlist.json")
        print(file_path)
        if not os.path.exists(file_path):
            return Response(
                {"error": "File does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        PlaylistData.objects.all().delete()
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            ids = data["id"]
            titles = data["title"]
            danceabilities = data["danceability"]
            energies = data["energy"]
            keys = data["key"]
            loudnesses = data["loudness"]
            modes = data["mode"]
            acousticnesses = data["acousticness"]
            instrumentalnesses = data["instrumentalness"]
            livenesses = data["liveness"]
            valences = data["valence"]
            tempos = data["tempo"]
            durations_ms = data["duration_ms"]
            time_signatures = data["time_signature"]
            num_bars = data["num_bars"]
            num_sections = data["num_sections"]
            num_segments = data["num_segments"]
            classes = data["class"]

            for key in ids.keys():
                PlaylistData.objects.create(
                    index=key,
                    id=ids[key],
                    title=titles[key],
                    danceability=danceabilities[key],
                    energy=energies[key],
                    key=keys[key],
                    loudness=loudnesses[key],
                    mode=modes[key],
                    acousticness=acousticnesses[key],
                    instrumentalness=instrumentalnesses[key],
                    liveness=livenesses[key],
                    valence=valences[key],
                    tempo=tempos[key],
                    duration_ms=durations_ms[key],
                    time_signature=time_signatures[key],
                    num_bars=num_bars[key],
                    num_sections=num_sections[key],
                    num_segments=num_segments[key],
                    class_field=classes[key],
                )

        return Response(
            {"message": "Data loaded successfully"}, status=status.HTTP_200_OK
        )


class PlaylistDataPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class PlaylistDataListView(APIView):
    pagination_class = PlaylistDataPagination

    def get(self, request, *args, **kwargs):
        queryset = PlaylistData.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PlaylistDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PlaylistDataDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            title = request.query_params.get('title')
            if title is None:
                return Response({"error":"title is missing"}, status=status.HTTP_404_NOT_FOUND)
            title = title.strip('\'"')
            Playlist_data = PlaylistData.objects.get(title=title)
            serializer = PlaylistDataSerializer(Playlist_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PlaylistData.DoesNotExist:
            return Response(
                {"error": f"Playlist with title '{title}' does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def patch(self, request, *args, **kwargs):
        try:
            title = request.query_params.get('title')
            if title is None:
                return Response({"error":"title is missing"}, status=status.HTTP_404_NOT_FOUND)
            title = title.strip('\'"')
            Playlist_data = PlaylistData.objects.get(title=title)
            star_rating = request.data.get("star_rating")
            if star_rating > 5 or star_rating < 1:
                return Response(
                    {"error": "provide a valid star rating"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if star_rating is not None:
                Playlist_data.star_rating = star_rating
                Playlist_data.save()
                return Response(
                    {"message": f"Star rating updated for Playlist '{title}'"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Star rating is required in the request body"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except PlaylistData.DoesNotExist:
            return Response(
                {"error": f"Playlist with title '{title}' does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
