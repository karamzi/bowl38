from datetime import timedelta
from rest_framework import serializers

from ..models import (
    News, CommentsModel, ReplyModels,
    ImgNews, Tournaments, OnlineRegistrations,
    TournamentComments, TournamentReply
)


class CustomDate(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    def get_date(self, obj):
        month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                      'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        date = obj.date + timedelta(hours=8)
        return f'{date.strftime("%H:%M")} {date.day} {month_list[date.month - 1]} {date.year}'


class ImgNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgNews
        fields = ('img',)


class NewsReplySerializer(CustomDate, serializers.ModelSerializer):
    class Meta:
        model = ReplyModels
        exclude = ('object_id',)


class NewsCommentSerializer(CustomDate, serializers.ModelSerializer):
    replyComments = NewsReplySerializer(many=True)

    class Meta:
        model = CommentsModel
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    link = serializers.SlugRelatedField(read_only=True, slug_field='link')
    img = ImgNewsSerializer(many=True)

    class Meta:
        model = News
        exclude = ('date', 'short_description')


class TournamentReplySerializer(CustomDate, serializers.ModelSerializer):
    class Meta:
        model = TournamentReply
        exclude = ('object_id',)


class TournamentCommentSerializer(CustomDate, serializers.ModelSerializer):
    replyComments = TournamentReplySerializer(many=True)

    class Meta:
        model = TournamentComments
        fields = "__all__"


class OnlineRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineRegistrations
        exclude = ('id', 'tournament')


class TournamentSerializer(serializers.ModelSerializer):
    results = serializers.SlugRelatedField(read_only=True, slug_field='link')

    class Meta:
        model = Tournaments
        exclude = ('date', 'show')
