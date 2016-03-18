# constellations/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from constellations.models import Constellation

class ConstellationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConstellationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-constellationform'
        self.helper.form_class = 'form-horizontal'
        self.label_class = 'col-xs-2'
        self.field_class = 'col-xs-6'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Save Record',
                                     css_class='btn btn-primary btn-medium',
                                     style='margin-top:10px;'))

    class Meta:
        model = Constellation
        fields = ('constellation_name', 'iau_abbr', 'other_abbr', 'genitive',
                  'family', 'origin', 'meaning', 'right_ascension',
                  'declination', 'number_of_stars', 'stars_with_planets',
                  'brightest_star',)

    def form_valid(self, form):
        success_url = '/constellations/'

    #TODO def form_invalid(self, form):
        #do this if the form is invalid
