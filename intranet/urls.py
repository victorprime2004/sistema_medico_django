from django.urls import path

from intranet import views

# exemplo: path('index/',views.index)
urlpatterns = [
    path('index/',views.index),
]


# VERBOS HTTPs - FRONT-END <-> BACKEND
# GET -> www.vollmed.com -> Exiba a página home do vollmed.
# POST -> www.vollmed.com -> Cadastrado um novo usuário.
# PUT -> www,vollmed.com/logado/alterar/1 -> Alterando o dado do usuário.
# DELETE -> www.vollmed.com/logado/deletar/1 -> Deletando um usuário.