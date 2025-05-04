from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercice, Workout, Reward
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.

@login_required
def dashboard(request):
    total_duration = Workout.objects.filter(user=request.user).aggregate(Sum('duration'))['duration__sum'] or 0
    workouts = Workout.objects.filter(user=request.user)
    reward = Reward.objects.filter(user=request.user)
    count = workouts.count()
    context = {
        'workouts' : workouts,
        'count' : count,
        'total_duration' : total_duration,
        'reward' : reward,
    }
    return render(request, 'pages/dashboard.html', context)

@login_required
def record_work(request):
    exercices = Exercice.objects.all()
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            exercice_id = request.POST.get('workoutType')
            workout.exercice = get_object_or_404(Exercice, id=exercice_id)            
            workout.save()
        else:
            print(form.errors)

    else:
        form = WorkoutForm()
    return render(request, 'pages/record_workout.html', {'form' : form, 'exercices' : exercices})

@login_required
def update_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    exercices = Exercice.objects.all()
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
        else:
            print(form.errors)

    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'pages/update_workout.html', {'form' : form, 'exercices' : exercices})

@login_required
def delete_workout(request, pk):
    workout = Workout.objects.filter(pk=pk)
    workout.delete()
    return JsonResponse({'message' : 'Plan of this exercice deleted!'})


def reward_system(request):
    user = request.user
    workout = Workout.objects.filter(user=user).last()

    reward = None
    if workout:
        reward, created = Reward.objects.get_or_create(user=user, workout=workout)
        if workout.complete and created:
            reward.points += 5
            reward.save()

    rewards = Reward.objects.filter(user=user)

    context = {
        'workout': workout,
        'rewards': rewards,
        'reward': reward,
    }
    return render(request, 'pages/reward.html', context)


def complete_workout(request, pk):
    user=request.user
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if not workout.complete:
        workout.complete = True
        workout.save()

        reward, created = Reward.objects.get_or_create(user=user, workout=workout)
        if created or reward.points == 0:
            reward.points += 5
            reward.save()

        
    return redirect('reward')