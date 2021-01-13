from django.db import models
from .utilities import get_img_path, get_patterns_path, get_tournaments_path, get_regulations_path


# Create your models here.


class Documents(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    link = models.URLField(verbose_name='Ссылка на результаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'
        ordering = ['-id']


class Results(models.Model):
    name = models.CharField(max_length=100, verbose_name='Турнир')
    link = models.URLField(verbose_name='Ссылка на результаты')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        ordering = ['-date']


class Patterns(models.Model):
    number = models.IntegerField(editable=True, verbose_name='Номер слота')
    img = models.ImageField(verbose_name='Изображение', upload_to=get_patterns_path)

    def __str__(self):
        return str(self.number) + ' диаграмма масла'

    class Meta:
        verbose_name = 'Программу масла'
        verbose_name_plural = 'Программы масла'
        ordering = ['number']


class RatingModel(models.Model):
    LEAGUE = (
        ('masters', 'Мастерс'),
        ('light', 'Лайт'),
        ('man', 'Мужчины'),
        ('women', 'Женщины'),
    )
    PLACE = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    league = models.CharField(max_length=10, choices=LEAGUE, verbose_name='Лига', default='masters')
    place = models.PositiveSmallIntegerField(choices=PLACE, verbose_name='Место')
    name = models.CharField(max_length=40, verbose_name='Игрок')
    score = models.PositiveSmallIntegerField(verbose_name='Очки')

    def __str__(self):
        return self.league

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название турнира')
    short_description = models.CharField(max_length=255, verbose_name='Описание для главной страницы')
    description = models.TextField(verbose_name='Контент')
    link = models.ForeignKey('Results', verbose_name='Ссылка', on_delete=models.SET_NULL, null=True,
                             related_name='news_link')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        for ai in self.ImgNews_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']


class ImgNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость', related_name='img')
    img = models.ImageField(upload_to=get_img_path, verbose_name='Изображение')

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class CommentsModel(models.Model):
    object_id = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments', verbose_name='id новости')
    username = models.CharField(max_length=40, verbose_name='Фамилия Имя')
    text = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date']


class ReplyModels(models.Model):
    object_id = models.ForeignKey('CommentsModel', on_delete=models.CASCADE, related_name='replyComments',
                                  verbose_name='id комментария')
    username = models.CharField(max_length=40, verbose_name='Фамилия Имя')
    text = models.TextField(verbose_name='Ответ')
    date = models.DateTimeField(auto_now_add=True)
    name_reply = models.CharField(max_length=40, verbose_name='Фамилия Имя', blank=True)

    class Meta:
        ordering = ['date']


class Tournaments(models.Model):
    STATUS = (
        (True, 'Да'),
        (False, 'Нет'),
    )
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tittle = models.CharField(max_length=50, verbose_name='Название турнира')
    description = models.TextField(verbose_name='Информация о турнире', blank=True)
    pattern = models.SmallIntegerField(verbose_name='Номер слота')
    img = models.ImageField(verbose_name='Изображение программы масла', upload_to=get_tournaments_path)
    results = models.ForeignKey('Results', verbose_name='Ссылка на результаты', on_delete=models.SET_NULL, null=True,
                                related_name='tournament_link', blank=True)
    status_registrations = models.BooleanField(verbose_name='Открыть регистрацию?', choices=STATUS, default=False)
    date = models.DateField(verbose_name='Дата')
    show = models.BooleanField(verbose_name='Показывать турнир на главной?', choices=STATUS, default=False)
    regulations = models.FileField(verbose_name='Регламент', upload_to=get_regulations_path)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-date']


class OnlineRegistrations(models.Model):
    GROUP = (
        (1, 'Первая группа'),
        (2, 'Вторая группа'),
        (3, 'Третья группа')
    )
    tournament = models.ForeignKey('Tournaments', related_name='list_players', verbose_name='Турнир',
                                   on_delete=models.CASCADE)
    group = models.SmallIntegerField(verbose_name='Группа', choices=GROUP, default=1)
    name = models.CharField(max_length=50, verbose_name='Игрок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Онлайн регистрация'
        verbose_name_plural = 'Онлайн регистрация'
        ordering = ['group', 'name']


class TournamentComments(models.Model):
    object_id = models.ForeignKey('Tournaments', on_delete=models.CASCADE, related_name='comments',
                                  verbose_name='Туринир')
    username = models.CharField(max_length=40, verbose_name='Фамилия Имя')
    text = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date']


class TournamentReply(models.Model):
    object_id = models.ForeignKey('TournamentComments', on_delete=models.CASCADE, related_name='replyComments',
                                  verbose_name='id комментария')
    username = models.CharField(max_length=40, verbose_name='Фамилия Имя')
    text = models.TextField(verbose_name='Ответ')
    date = models.DateTimeField(auto_now_add=True)
    name_reply = models.CharField(max_length=40, verbose_name='Фамилия Имя', blank=True)

    class Meta:
        ordering = ['date']
