from pandas.io.parsers import read_csv
from rest_framework import serializers
from .models import Lyrics
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import LyricsSerializer, SearchSerializer
from .models import Lyrics

from .docuSim import *
from django.contrib.staticfiles import finders
import json


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Data': {
            'Song': 'Taylor Swift',
            'Lyrics': 'Lyrics go here',
            'Artist': 'Artist name goes here'
        }

    }
    return Response(api_urls)


@api_view(['GET'])
def lyricList(request):
    tasks = Lyrics.objects.all()
    serializer = LyricsSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def search(request):
    print(request)
    tasks = Lyrics.objects.all()
    if tasks is not None:
        tasks.delete()
    serializer = SearchSerializer(data=request.data)
    if serializer.is_valid():
        keyword = serializer.validated_data['keyword']
        if keyword:
            lyrics_loc = "data\lyrics.csv"
            data_path = finders.find(lyrics_loc)
            print(data_path)
            searc_loc = finders.searched_locations
            print("Locations: %s" % searc_loc)
            if len(searc_loc) > 0:
                lyrics_path = "%s\%s" % (
                    searc_loc[0], lyrics_loc)
                print(lyrics_path)
                dataframe = read_csv(lyrics_path)
                lyrics_ids = tfidf(keyword, dataframe)
                print(lyrics_ids)
            for lyric in lyrics_ids:
                print(lyric)
                context = {
                    "artist": dataframe.loc[lyric, 'Artist Name'],
                    "song": dataframe.loc[lyric, 'Song Name'],
                    "lyrics": dataframe.loc[lyric, 'Lyrics']
                }

                print(context)

                serializer = LyricsSerializer(data=context)
                if serializer.is_valid():
                    serializer.save()
        return Response(serializer.data)
    return Response("serializer.data")


"""
tasks = Lyrics.objects.all()
    tasks.delete()
"""
