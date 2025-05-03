from django import forms
from .models import Exercice, Workout



class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('title', 'number_of_repetitions', 'sets', 'weigth', 'date', 'duration', 'workout_notes', 'start', 'end', 'complete', 'rating', )
        widgets = {
            'start' : forms.TimeInput(attrs={'type' : 'time'}),
            'end' : forms.TimeInput(attrs={'type' : 'time'})
        }