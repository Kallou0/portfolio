from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm

# Create your views here.
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})