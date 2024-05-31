from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Appointment




def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        user = authenticate(request, username=cpf, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid CPF or password'})
    return render(request, 'login.html')


def transicaocadastro(request):
    return render(request,'cadastro/cadastro.html',{})

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario(
            nome=request.POST.get('nome'),
            nascimento=request.POST.get('nascimento'),
            cpf=request.POST.get('cpf'),
            email=request.POST.get('email'),
            endereco=request.POST.get('endereco'),
            doenca=request.POST.get('doenca'),
            password=request.POST.get('password')
        )
        novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'cadastro/usuarios.html', usuarios)

@login_required
def home(request):
    appointments = Appointment.objects.all()
    return render(request, 'home.html', {'appointments': appointments})

@login_required
def user_profile(request):
    user_appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'user': request.user, 'appointments': user_appointments})

@login_required
def book_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.user = request.user
    appointment.save()
    return redirect('home')

@login_required
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id, user=request.user)
    if appointment:
        appointment.cancel()
    return redirect('user_profile')

def login_view(request):
    return render(request, 'app_cad_usuarios/login.html')

def existing_login_view(request):
    # Lógica adicional aqui
    return render(request, 'app_cad_usuarios/login.html')