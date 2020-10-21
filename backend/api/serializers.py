from django.db.models import fields
from rest_framework import serializers
from .models import Lyrics, Search


class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics #model used to return the result to the user
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search #model to take the input keyword from the user
        fields = '__all__'
