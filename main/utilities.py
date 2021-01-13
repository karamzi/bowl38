from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    pass


def get_regulations_path(instance, filename):
    return 'regulations/%s/%s%s' % (instance.id, datetime.now().timestamp(), splitext(filename)[1])


def get_img_path(instance, filename):
    return 'news/%s/%s%s' % (instance.news.pk, datetime.now().timestamp(), splitext(filename)[1])


def get_patterns_path(instance, filename):
    return 'pattern/pattern_%s_%s%s' % (instance.number, datetime.now().timestamp(), splitext(filename)[1])


def get_tournaments_path(instance, filename):
    return 'tournament/%s/%s%s' % (instance.id, datetime.now().timestamp(), splitext(filename)[1])
