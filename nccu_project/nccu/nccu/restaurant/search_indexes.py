import datetime
from haystack import indexes
from restaurant.models import Restaurant


class RestaurantIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    address= indexes.CharField()
   

    def get_model(self):
        return Restaurant

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()