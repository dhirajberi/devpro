from django.forms import ModelForm, widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('vote_ratio', 'vote_total')

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
