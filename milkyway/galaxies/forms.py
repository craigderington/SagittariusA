# galaxies/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Galaxy


class GalaxyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalaxyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-galaxyform'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Record',
                                     css_class='btn btn-medium btn-primary',
                                     style="margin-top:10px"))

    class Meta:
        model = Galaxy
        fields = ('galaxy_name', 'distance', 'notes', 'constellation')

    def form_valid(self):
        success_url = '/galaxies/'
