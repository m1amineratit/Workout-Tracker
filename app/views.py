from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercice, Workout
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    workouts = Workout.objects.filter(user=request.user)
    count = workouts.count()
    context = {
        'workouts' : workouts,
        'count' : count,
    }
    return render(request, 'pages/dashboard.html', context)

@login_required
def record_work(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
        else:
            print(form.errors)

    else:
        form = WorkoutForm()
    return render(request, 'pages/record_workout.html', {'form' : form})

@login_required
def update_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
        else:
            print(form.errors)

    else:
        form = WorkoutForm()
    return render(request, 'pages/update_workout.html', {'form' : form})

@login_required
def delete_workout(request, pk):
    workout = Workout.objects.filter(pk=pk)
    workout.delete()
    return JsonResponse({'message' : 'Plan of this exercice deleted!'})

