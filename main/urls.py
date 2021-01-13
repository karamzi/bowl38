from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView
from .views import AllNewsView
from .views import AllTournamentView
from .views import calendar
from .views import club_300
from .views import documents
from .views import current_news
from .views import patterns
from .views import results
from .views import MainUserLogin
from .views import RegistrationUserView
from .views import MainLogoutView
from .views import current_tournament

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/1.0/', include('main.API.urls')),
    path('all_news/', AllNewsView.as_view(), name='all_news'),
    path('all_tournaments/', AllTournamentView.as_view(), name='all_tournaments'),
    path('calendar/', calendar, name='calendar'),
    path('club_300/', club_300, name='club_300'),
    path('documents/', documents, name='documents'),
    path('news/<int:news_id>/', current_news, name='current_news'),
    path('patterns/', patterns, name='patterns'),
    path('results/', results, name='results'),
    path('accounts/login/', MainUserLogin.as_view(), name='login'),
    path('accounts/logout/', MainLogoutView.as_view(), name='logout'),
    path('accounts/registration/', RegistrationUserView.as_view(), name='registrations'),
    path('tournament/<int:tournament_id>/', current_tournament, name='current_tournament'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
