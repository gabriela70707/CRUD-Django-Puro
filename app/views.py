from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonagensHarryPotter
from .forms import PersonagemForm

def listar_personagens(request):
    personagens = PersonagensHarryPotter.objects.all()
    return render(request, 'listagem.html', {'personagens':personagens})

def criar_bruxo(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
        return render(request, 'formulario.html', {"formulario":form})
    

def atualizar_bruxo(request, pk):
    bruxo = get_object_or_404(PersonagensHarryPotter, pk=pk)
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=bruxo)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:  # Aqui tratamos o método GET
        form = PersonagemForm(instance=bruxo)
        
    return render(request, 'formulario.html', {'formulario': form})


def deletar_bruxo(request, pk):
    bruxo = get_object_or_404(PersonagensHarryPotter, pk=pk)
    if request.method == 'POST':
        bruxo.delete()
        return redirect('listar_personagens')
    return render (request, 'confirmar_delete.html', {'bruxo':bruxo})
