from django.shortcuts import render




def index(request):

    provas = {
        1:'Banco de dados',
        2:'POO',
        3:'Segurança'
        }
    dados = {
        'nome_da_prova' : provas
        }
    return render(request,'index.html',dados)

def prova(request):
    return render(request,'prova.html')

