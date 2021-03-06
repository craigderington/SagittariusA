from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from stars.models import Star

class StarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StarForm, self).__init__(*args, **kwargs)
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
        model = Star
        fields = ('proper_name', 'distance', 'bayer_designation',
                  'spectral_class', 'magnitude', 'evolution_stage',)

    def form_valid(self, form):
        success_url = '/stars/'

    #TODO def form_invalid(self, form):
        #do this if the form is invalid
