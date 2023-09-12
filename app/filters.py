import django_filters

from .models import ExtendUser

class ExtendUserFilter(django_filters.FilterSet):
    class Meta:
        model = ExtendUser
        fields = '__all__'