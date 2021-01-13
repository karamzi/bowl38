import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import Documents
from .models import Results
from .models import News
from .models import Patterns
from .models import RatingModel
from .models import Tournaments
from .forms import RegisterUserForm, LoginUserForm


class IndexView(View):
    """Главная страница"""

    def get(self, request):
        last_results = Tournaments.objects.filter(date__lt=datetime.date.today())[:3]
        news = News.objects.all()[:3]
        masters = RatingModel.objects.filter(league='masters')
        light = RatingModel.objects.filter(league='light')
        man = RatingModel.objects.filter(league='man')
        women = RatingModel.objects.filter(league='women')
        tournaments = Tournaments.objects.filter(show=True, date__gte=datetime.date.today()).order_by('date')[:3]
        context = {
            'last_results': last_results,
            'news': news,
            'masters': masters,
            'light': light,
            'man': man,
            'women': women,
            'tournaments': tournaments,
        }
        return render(request, 'main/index.html', context)


class AllNewsView(ListView):
    template_name = 'main/all_news.html'
    model = News
    paginate_by = 5


class AllTournamentView(ListView):
    template_name = 'main/all_tournaments.html'
    model = Tournaments
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_tournaments'] = []
        context['past_tournaments'] = []
        for tournament in context['tournaments_list']:
            if tournament.date >= datetime.date.today():
                context['future_tournaments'].append(tournament)
            else:
                context['past_tournaments'].append(tournament)
        return context


def calendar(request):
    """Календарь"""
    return render(request, 'main/calendar.html')


def club_300(request):
    """Клуб 300"""
    return render(request, 'main/club_300.html')


def documents(request):
    """Документы"""
    documents = Documents.objects.all()
    context = {'documents': documents}
    return render(request, 'main/documents.html', context)


def current_news(request, news_id):
    """Определенная новость"""
    news = News.objects.get(pk=news_id)
    return render(request, 'main/news.html', {'news': news})


def patterns(request):
    """Программы масла"""
    patterns = Patterns.objects.all()
    context = {'patterns': patterns}
    return render(request, 'main/patterns.html', context)


def results(request):
    """Результаты"""
    results = Results.objects.all()
    context = {'results': results}
    return render(request, 'main/results.html', context)


def current_tournament(request, tournament_id):
    """Страница туринира"""
    tournament = Tournaments.objects.get(pk=tournament_id)
    return render(request, 'main/tournament.html', {'tournament': tournament})


class MainUserLogin(LoginView):
    """Авторизация пользователя"""
    form_class = LoginUserForm
    template_name = 'main/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:index')


class RegistrationUserView(SuccessMessageMixin, CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = RegisterUserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('main:login')
    success_message = 'Вы успешно зарегистрированы! Ожидайте активации администратором'


class MainLogoutView(LoginRequiredMixin, LogoutView):
    """Выход из аккаунта"""
    next_page = reverse_lazy('main:login')
