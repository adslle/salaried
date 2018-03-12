from django import forms

from bu.models import BU


class BUForm(forms.ModelForm):

    class Meta:
        model = BU

        fields = [
            'name',
            'description',
            'manager'
        ]

    def __init__(self, *args, **kwargs):
        super(BUForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'materialize-textarea'})