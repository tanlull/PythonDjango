from rest_framework import serializers
from countries.models import Countries

class CountriesSerializer(serializer.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id','name','capital')