from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.


User = get_user_model()

class Exercice(models.Model):
    STATUS_CHOICE = (
        ('cardio', 'Cardio'),
        ('strength' , 'Strength'),
        ('flexibility' , 'Flexibility')
    )
    MUSCLE_GROUP = (
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('legs' , 'Legs'),
        ('shoulders' , 'Shoulders'),
        ('full body' , 'Full Body')
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=STATUS_CHOICE)
    muscle = models.CharField(max_length=100, choices=MUSCLE_GROUP)

    def __str__(self):
        return f"Exercice on {self.category}, type ({self.muscle})"
    
class Workout(models.Model):
    class Rating(models.IntegerChoices):
        VERY_BAD = 1, 'Very Bad'
        BAD = 2, 'Bad'
        OKAY = 3, 'Okay'
        GOOD = 4, 'Good'
        EXCELLENT = 5, 'Excellent'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_repetitions = models.IntegerField(default=1)
    sets = models.IntegerField(default=0)
    weigth = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    duration = models.IntegerField()
    workout_notes = models.TextField()
    start = models.TimeField()
    end = models.TimeField()
    complete = models.BooleanField(default=False, blank=True, null=True)
    rating = models.IntegerField(choices=Rating.choices, default=3)

    def time_to_second(self, time_obj):
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    
    
    def get_duration_minutes(self):
        start_seconds = (self.time_to_second(self.start))
        end_seconds = (self.time_to_second(self.end))

        if end_seconds < start_seconds:
            end_seconds += 24 * 3600
            self.complete = True
    
        duration = end_seconds - start_seconds
        return duration / 60

    def get_calcult_duration(self):
        start_seconds = (self.time_to_second(self.start))
        end_seconds = (self.time_to_second(self.end))

        if end_seconds < start_seconds:
            end_seconds += 24 * 3600
            self.complete = True
    
        duration = end_seconds + start_seconds
        return duration / 60
