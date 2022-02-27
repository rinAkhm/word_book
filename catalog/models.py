from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите жанр книги',
                            verbose_name='Жанр книги')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Введите язык книги',
                            verbose_name='Язык книги')

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text='Введите фамилию автора',
                                  verbose_name='Имя автора')

    last_name = models.CharField(max_length=100,
                                 help_text='Введите фамилию автора',
                                 verbose_name='Фамилию автора')

    date_of_birth = models.DateField(help_text='Введите дату рождения',
                                     verbose_name='Дата рождения',
                                     null=True, blank=True)

    date_of_death = models.DateField(help_text='Введите дату смерти',
                                     verbose_name='Дата смерти',
                                     null=True, blank=True)

    def __str__(self):
        return self.lastname

class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Введите назвние книги',
                             verbose_name='Назвние книги')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text='Выберите жанр для книги',
                              verbose_name='Жанр книги', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text='Выберите язык книги',
                                 verbose_name='Язык книги', null=True)

    author = models.ManyToManyField('Author',
                                    help_text='Выберите автора книги',
                                    verbose_name='Автор книги', null=True)

    summary = models.TextField(max_length=1000,
                               help_text='Введите краткое описание книги',
                               verbose_name='Аннотация книги')

    isbn = models.CharField(max_length=13,
                            help_text='Должно содержать 13 символов',
                            verbose_name='ISBN книги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

