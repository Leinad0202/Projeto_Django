from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = UsuarioForm()

    if request.method == 'GET' and 'apagar' in request.GET:
        usuario_id = request.GET['apagar']
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            usuario.delete()
            return redirect('listagem_usuarios')
        except Usuario.DoesNotExist:
            # Lidar com o caso em que o usuário não foi encontrado
            pass

    usuarios = {
        'usuarios': Usuario.objects.all(),
        'form': form
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def home(request):
    form = UsuarioForm()  # Crie uma instância do seu formulário

    if request.method == 'POST':
        form = UsuarioForm(request.POST)  # Passe os dados do POST para o formulário

        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
        else:
            erro_mensagem = 'Por favor, corrija os erros no formulário.'

    context = {
        'form': form,
        'erro_mensagem': erro_mensagem if 'erro_mensagem' in locals() else None  # Certifique-se de que erro_mensagem esteja definido
    }

    return render(request, 'usuarios/home.html', context)

def info(request):
    # Lógica para buscar as informações que deseja exibir na página info.html
    # Por exemplo:
    info_data = "Alguma informação relevante"

    return render(request, 'usuarios/info.html', {'info_data': info_data})