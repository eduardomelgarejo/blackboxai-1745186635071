from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_secretary(user):
    return user.tipo_usuario == 'ambos' or (user.tipo_usuario == 'paciente' and hasattr(user, 'secretary_profile'))

def is_administrator(user):
    return user.is_superuser or user.is_staff

def is_professional(user):
    return user.tipo_usuario == 'profesional' or user.tipo_usuario == 'ambos'

@login_required
@user_passes_test(is_secretary)
def secretary_dashboard(request):
    return render(request, 'secretary_dashboard.html')

@login_required
@user_passes_test(is_administrator)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(is_professional)
def professional_dashboard(request):
    return render(request, 'professional_dashboard.html')
