from django.forms import ModelForm, DateInput
from .models import Qcreport

class EventForm(ModelForm):
  class Meta:
    model = Qcreport
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date_posted': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['date_posted'].input_formats = ('%Y-%m-%dT%H:%M',)
    