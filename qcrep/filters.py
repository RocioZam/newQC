import django_filters
from django_filters import DateFilter
from .models import Qcreport


class QcFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    date_posted = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Qcreport
        fields = ('title', 'client', 'author', 'status', 'date_posted')


