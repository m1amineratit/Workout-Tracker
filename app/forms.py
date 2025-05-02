from django import forms
from .models import Exercice, Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('exercice', 'number_of_repetitions', 'sets', 'weigth', 'start', 'end', )
        widgets = {
            'start' : forms.TimeInput(attrs={'type' : 'time'}),
            'end' : forms.TimeInput(attrs={'type' : 'time'})
        }