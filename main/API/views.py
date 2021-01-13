from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist

from ..models import News, CommentsModel, ReplyModels, Tournaments, OnlineRegistrations, TournamentComments, \
    TournamentReply
from .serializers import (
    NewsSerializer, NewsCommentSerializer, TournamentSerializer,
    OnlineRegistrationSerializer, TournamentCommentSerializer
)


class NewsView(APIView):

    def get(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
            comments = news.comments.all()
            user = request.user.first_name + ' ' + request.user.last_name if request.user.is_authenticated else ''
            news_serializer = NewsSerializer(news)
            comments_serializer = NewsCommentSerializer(comments, many=True)
            return Response({
                'status': 200,
                'user': user,
                'isStaff': request.user.is_staff,
                'news': news_serializer.data,
                'comments': comments_serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Новость не найдена'
            })


class TournamentView(APIView):

    def get(self, request, pk):
        try:
            tournament = Tournaments.objects.get(pk=pk)
            players = tournament.list_players.all()
            tournament_comments = tournament.comments.all()
            user = request.user.first_name + ' ' + request.user.last_name if request.user.is_authenticated else ''
            tournament_serializer = TournamentSerializer(tournament)
            players_serializer = OnlineRegistrationSerializer(players, many=True)
            comment_serializer = TournamentCommentSerializer(tournament_comments, many=True)
            return Response({
                'status': 200,
                'user': user,
                'isStaff': request.user.is_staff,
                'tournament': tournament_serializer.data,
                'online_registrations': players_serializer.data,
                'comments': comment_serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Турнир не найден',
            })


class OnlineRegistrationsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not OnlineRegistrations.objects.filter(tournament=request.POST['id'],
                                                  name=request.user.first_name + ' ' + request.user.last_name).exists():
            if OnlineRegistrations.objects.filter(group=request.POST['group']).count() < 16:
                player = OnlineRegistrations()
                player.tournament_id = request.POST['id']
                player.name = request.user.first_name + ' ' + request.user.last_name
                player.group = request.POST['group']
                player.save()
                return Response({
                    'status': 200,
                    'message': 'Игрок был зарегистрирован'
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Нет свободных мест в группе'
                })
        else:
            return Response({
                'status': 400,
                'message': 'Игрок уже зарегистрирован'
            })

    def delete(self, request):
        try:
            player = OnlineRegistrations.objects.get(tournament=request.GET['id'],
                                                     name=request.user.first_name + ' ' + request.user.last_name)
            player.delete()
            return Response({
                'status': 200,
                'message': 'Игрок был удален'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 400,
                'message': 'Игрок отсутствует'
            })


class Comment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        comment = self.model()
        comment.object_id_id = int(request.POST['id'])
        comment.username = request.user.first_name + ' ' + request.user.last_name
        comment.text = request.POST['text']
        comment.save()
        return Response({
            'status': 200,
            'message': 'Комментарий добавлен',
        })

    def put(self, request):
        try:
            comment = self.model.objects.get(pk=int(request.POST['id']))
            comment.text = request.POST['text']
            comment.save()
            return Response({
                'status': 200,
                'message': 'Комментарий был изменен'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Комментарий не найден'
            })

    def delete(self, request):
        try:
            comment = self.model.objects.get(pk=int(request.GET['id']))
            comment.delete()
            return Response({
                'status': 200,
                'message': 'Комментарий был удален'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Комментарий не найден'
            })


class Reply(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        reply = self.model()
        reply.object_id_id = int(request.POST['id'])
        reply.username = request.user.first_name + ' ' + request.user.last_name
        reply.text = request.POST['text']
        reply.name_reply = request.POST['name_reply']
        reply.save()
        return Response({
            'status': 200,
            'message': 'Ответ был добавлен'
        })

    def put(self, request):
        try:
            reply = self.model.objects.get(pk=int(request.POST['id']))
            reply.text = request.POST['text']
            reply.save()
            return Response({
                'status': 200,
                'message': 'Ответ был изменен'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Ответ не найден'
            })

    def delete(self, request):
        try:
            reply = self.model.objects.get(pk=int(request.GET['id']))
            reply.delete()
            return Response({
                'status': 200,
                'message': 'Ответ был удален'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': 404,
                'message': 'Ответ не найден'
            })


class NewsCommentView(Comment):
    model = CommentsModel


class NewsReplyView(Reply):
    model = ReplyModels


class TournamentCommentView(Comment):
    model = TournamentComments


class TournamentCommentViewReplyView(Reply):
    model = TournamentReply
