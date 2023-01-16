from django.apps import AppConfig
from django.urls import register_converter
from .converters import DateConverter


class BookConfig(AppConfig):
    name = 'books'

    '''
    функция ready исполняется один раз при запуске приложения
    '''
    def ready(self):
        register_converter(DateConverter, 'my_cvt')
