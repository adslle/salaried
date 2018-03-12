from django import forms

from bu.models import BU
from salaried.models import Document
from .models import Salaried


class SalariedForm(forms.ModelForm):
    # bu = forms.ModelChoiceField(queryset=BU.objects.all(), empty_label='Select a Business unit')


    class Meta:
        model = Salaried
        fields = [
            'first_name',
            'last_name',
            'cin_code',
            'birth_day',
            'hire_day',
            'email',
            'cnss_code',
            'bu',
        ]

    def __init__(self, *args, **kwargs):
        super(SalariedForm, self).__init__(*args, **kwargs)
        #self.initial_email = self.email
        # print( "------------------------------",self.email)
        self.fields['bu'].label = "Business unit"
        self.fields['birth_day'].widget.attrs.update({'class': 'datepicker'})
        self.fields['hire_day'].widget.attrs.update({'class': 'datepicker'})

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'label',
            'description',
            'attached_piece'
        ]

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        # self.fields['description'].widget.attrs.update({'class': 'materialize-textarea'})
        self.fields['attached_piece'].widget.attrs.update({'class': 'file-input'})
        # self.fields['attached_piece'].label = "CV"
        self.fields['description'].widget.attrs.update({'class': 'materialize-textarea'})
        self.fields['attached_piece'].label = "attached piece"
