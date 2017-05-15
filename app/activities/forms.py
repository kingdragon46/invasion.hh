from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Activity
from events.models import Invader, get_current_invasion


class SelectActivitiesForm(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.filter(invasion=get_current_invasion()))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Invader
        fields = ('activities',)
