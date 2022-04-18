from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import AdicionarTarefa, EditarTarefaForm

# Create your views here.

# Retorna as tarefas pendentes
def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html', {'tarefas_pendentes':tarefas_pendentes, 'form':form})

# Função de concluir a tarefa
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Função de excluir a tarefa
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')

# Função de adiar a tarefa
def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Função de editar a tarefa
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(initial={'tarefa':tarefa.descricao, 'categoria':tarefa.categoria})
    return render(request, 'tarefas/editar_tarefa.html', {'tarefa':tarefa, 'form':form} )

# Função para exibir a tarefas concluídas
def tarefas_concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluído')
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluidas':tarefas_concluidas})

# Função para exibir a tarefas adiadas
def tarefas_adiadas_list(request):
    tarefas_adiadas = Tarefa.objects.filter(status='adiado')
    return render(request, 'tarefas/tarefas_adiadas.html', {'tarefas_adiadas':tarefas_adiadas})

# Função para mover tarefas de adiadas para lista de tarefas
def mover_para_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Função da pagina adicionar_tarefas
def adicionar_tarefas(request):
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar_tarefas')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/adicionar_tarefas.html', {'adicionar_tarefas':adicionar_tarefas, 'form':form})
