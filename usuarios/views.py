from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth  import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from usuarios.forms import BancoForm, PerfilForm, UserCreateForm




def login_page(request):
	if not request.user.is_anonymous():
		return render_to_response('home.html',context_instance=RequestContext(request))
	
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			
			if username=='' or password=='':
				return render_to_response('usuarios/login.html',{'message':'Alguno de los campos esta vacio!'},
																context_instance=RequestContext(request))
			acceso = authenticate(username = username, password = password)
			if acceso.is_active:
				login(request, acceso)
				return render_to_response('home.html',context_instance=RequestContext(request))
			else:
				return render_to_response('usuarios/login.html',{'message':'El usuario no esta activo por favor verifiquelo con el administrador del sistema'},
																context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('usuarios/login.html',{'formulario':formulario},context_instance = RequestContext(request))


@login_required(login_url="/login/")
def home(request):
	message = 'Mensaje 1'
	return render_to_response('home.html',context_instance=RequestContext(request))


def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def banco(request):
	formulario = BancoForm()
	return render_to_response('banco/bancopy.html',{'formulario':formulario},context_instance = RequestContext(request))


def usuario_nuevo(request):
	if request.method == 'POST':
		formulario =  UserCreateForm()
		if formulario.is_valid:
			formulario.save()
			formulario = UserCreateForm()
			return HttpResponseRedirect('/definir/usuarios/lista/')
	else:
		formulario_user  = 	 UserCreateForm()
		formulario_perfil =  PerfilForm()
		message = "Si estan pasando"
		return render_to_response('usuarios/perfil.html',{ 'formulario': formulario_perfil,'formulario1':formulario_user,	
													   'message': message }, context_instance =  RequestContext(request))

def listar_usuarios(request):
	usuarios = User.objects.all().order_by('last_name')
	return render_to_response('usuarios/list_user.html',{'usuarios':usuarios}, context_instance = RequestContext(request))