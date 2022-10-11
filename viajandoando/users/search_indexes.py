from haystack import indexes
from users.models import *

class UsuarioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre = indexes.CharField(model_attr='username')
    id = indexes.CharField(model_attr='id')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


# class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     titulo = indexes.CharField(model_attr='titulo')
#     fecha = indexes.DateTimeField(model_attr='fecha')

#     def get_model(self):
#         return Noticia

#     def index_queryset(self, using=None):
#         """Queremos que se indexen todas las noticias que tengan archivada=False"""
#         return self.get_model().objects.filter(archivada=False)