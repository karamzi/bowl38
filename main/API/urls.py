from django.urls import path

from .views import NewsView, NewsCommentView, NewsReplyView, TournamentView, OnlineRegistrationsView, \
    TournamentCommentView, TournamentCommentViewReplyView, BotAPI

urlpatterns = [
    path('news/<int:pk>/', NewsView.as_view()),
    path('news/comment/', NewsCommentView.as_view()),
    path('news/reply/', NewsReplyView.as_view()),
    path('tournament/<int:pk>/', TournamentView.as_view()),
    path('tournament/comment/', TournamentCommentView.as_view()),
    path('tournament/reply/', TournamentCommentViewReplyView.as_view()),
    path('online_registrations/', OnlineRegistrationsView.as_view()),
    path('bot/', BotAPI.as_view()),
]
