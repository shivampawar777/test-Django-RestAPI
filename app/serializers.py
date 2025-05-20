from rest_framework import serializers
from app.models import Person, Colour

class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ['c_name']


class PersonSerializer(serializers.ModelSerializer):
    color = ColourSerializer()
    colorInfo = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    
    def get_colorInfo(self, obj):
        colorInfo_obj = Colour.objects.get(id=obj.color.id)

        return {'c_name' : colorInfo_obj.c_name, 'Hex Code' : '#000'}


    def validate_name(self, name):
        special_chars = "@_!#$%^&*()<>?/\|}{~:"

        if any(c in special_chars for c in name):
            raise serializers.ValidationError("No special characters allowed in name")

        return name
    
    def validate_age(self, age):
        if (age < 18 or age > 60):
            raise serializers.ValidationError("Age must be between 18 and 60")
        
        return age


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

