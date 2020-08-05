from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.utils.safestring import SafeData, SafeString, mark_safe
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Subquery  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
    TemplateView
)
from .models import Qcreport, UsersChart
from users.models import Profile
from .filters import QcFilter
from .utils import Calendar
from PIL import Image
import html
import calendar


# Create your views here.
def home (request):
    #get just the last three records.
    context = {
        'qcreports': Qcreport.objects.all().order_by('-id')[:3]
    }
    return render (request, 'qcrep/home.html', context)


class QcreportListView(ListView):
    model = Qcreport
    template_name = 'qcrep/qcreport_list.html'
    context_object_name = 'qcreports'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = QcFilter(self.request.GET, queryset=self.get_queryset())
        return context



class UserQcListView(ListView):
    model = Qcreport
    template_name = 'qcrep/user_qc_list.html'
    context_object_name = 'qcreports'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Qcreport.objects.filter(author=user).order_by('-date_posted')

    
    

class QcreportDetailView(DetailView):
    model = Qcreport
    template_name = 'qcrep/qc_detail.html'
    context_object_name = 'qcreports'


class QcreportCreateView(LoginRequiredMixin, CreateView):
    model = Qcreport
    template_name = 'qcrep/qcreports_form.html'
    context_object_name = 'qcreports'
    fields = ['title', 'client',  'filename', 'status', 'aspect', 'codec', 'bit', 'resolution', 'conmments', 
    'framesPerSecond', 'tecreject', 'missing_elements', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QcreportUpdateView(LoginRequiredMixin, UpdateView):
    model = Qcreport
    template_name = 'qcrep/qcreports_form.html'
    context_object_name = 'qcreports'
    fields = ['title', 'client', 'filename', 'status', 'aspect', 'codec', 'bit', 'resolution', 'conmments', 
    'framesPerSecond', 'tecreject', 'missing_elements', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




    
def user_reports (request):
    #get list of users with it's qcreports reviews
    context = {
        'users': User.objects.all(),    
        #'qcreports': Qcreport.objects.all(),
        #'qcreports': Qcreport.objects.filter(date_posted__year=2020),
        'user_qc' : User.objects.annotate(total_qcreports = Count('qcreport')),
        'total_qc':Qcreport.objects.count()
    }
    
    return render (request, 'qcrep/user_reports.html', context)
      
    


def about (request):
    model = Qcreport   
    context = {    
        'qcreports': Qcreport.objects.values('author','author__username', 'author__profile')
        .filter(date_posted__year=2019)
        .annotate(total_qcreports = Count('author')),   
        'total_qc':Qcreport.objects.filter(date_posted__year=2019).count()                             
    }
    return render (request, 'qcrep/about.html', context)


def KPI_2020 (request):
    model = Qcreport  
    context = {      
         'qcreports': Qcreport.objects.values('author','author__username')
        .filter(date_posted__year=2020)
        .annotate(total_qcreports = Count('author')),
        'total_qc':Qcreport.objects.filter(date_posted__year=2020).count(),   
                              
    }
    return render (request, 'qcrep/KPI_2020.html', context)


def client (request):
    model = Qcreport  
    context = {      
         'qcreports': Qcreport.objects.values('client')       
        .annotate(total_qcreports = Count('client')),
        'total_qc':Qcreport.objects.count()  
                                    
    }
    return render (request, 'qcrep/client.html', context)


class CalendarView(ListView):
    model = Qcreport
    template_name = 'qcrep/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

