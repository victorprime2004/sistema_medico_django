from django.shortcuts import render

# GET,POST,PUT, DELETE
# REQUEST <-> RESPONSE
# render -> RENDERIZAR


# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request): # É o request feita pelo usuário
    return render(
        request,
        'templates/intranet/index.html'
    )