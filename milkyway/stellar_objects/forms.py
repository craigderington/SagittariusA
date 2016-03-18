# stellar_objects/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import StellarObject

class StellarObjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StellarObjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-starform'
        self.helper.form_class = 'form-horizontal'
        self.label_class = 'col-xs-2'
        self.field_class = 'col-xs-6'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Save Record',
                                     css_class='btn btn-primary btn-medium',
                                     style='margin-top:10px;'))

    class Meta:
        model = StellarObject
        fields = ('name', 'distance', 'stellar_object_type', 'constellation',)

    def form_valid(self, form):
        success_url = '/stellar_objects/'

    #TODO def form_invalid(self, form):
        #do this if the form is invalid
