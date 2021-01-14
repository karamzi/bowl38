from django.contrib import admin
from .models import Documents
from .models import Results
from .models import News
from .models import ImgNews
from .models import Patterns
from .models import RatingModel
from .models import Tournaments
from .models import OnlineRegistrations
from django import forms
from ckeditor.widgets import CKEditorWidget


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('name', 'link')
    search_fields = ('name',)


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'date')
    list_display_links = ('name', 'link')
    search_fields = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'date')
    list_display_links = ('title', 'short_description')
    search_fields = ('title',)
    form = NewsAdminForm


class ImgNewsAdmin(admin.ModelAdmin):
    list_display = ('news', 'img')


class PatternsAdmin(admin.ModelAdmin):
    list_display = ('number', 'img')
    list_display_links = ('number',)
    search_fields = ('number',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('league', 'place', 'name', 'score')
    search_fields = ('name',)
    list_editable = ('name', 'score')
    readonly_fields = ('league', 'place')


class OnlineRegistrationsAdmin(admin.TabularInline):
    model = OnlineRegistrations
    extra = 1


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'description', 'pattern', 'status_registrations', 'show', 'date')
    list_display_links = ('tittle', 'description', 'pattern', 'status_registrations', 'show')
    search_fields = ('title',)
    inlines = [OnlineRegistrationsAdmin]


admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(ImgNews, ImgNewsAdmin)
admin.site.register(Patterns, PatternsAdmin)
admin.site.register(RatingModel, RatingAdmin)
admin.site.register(Tournaments, TournamentAdmin)
