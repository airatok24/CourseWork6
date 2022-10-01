from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model =Ad
        fields = ("pk", "image", "title", "price", "description", )


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
