from django.utils import timezone # Importação do módulo

from django.db import models

# Criar um modelo do médico, com nome, email, telefone, crm, especialidade
class Medico(models.Model):
    # Atributos = características = variáveis
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default = timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default = True)
    mensagem = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%y/%m', blank=True)

    # Métodos = ações = funções
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
   #================================================================= 
# Criando um modelo do Paciente, com nome, email, telefone e cpf
class Paciente(models.Model):
    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length= 15)
    cpf = models.CharField(max_length= 11)
    criacao_data = models.DateTimeField(default= timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default = True)
    imagem = models.ImageField('img/%Y/%m', blank=True)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    

class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    medico_id = models.ForeignKey(Medico,on_delete=models.CASCADE)
    horario = models.DateField(default=timezone.now)
    obaservacao = models.TextField(blank=True)
    status = models.CharField(
        default ='A',   
        max_length = 1,
        choices =(
            ('A','Agendando'),
            ('X','Cancelado'),
            ('C','Confirmado'),
            ('R','Realizado'),
        )
    )

def __str__(self):
        return f'{self.status} com sucesso'
    
    

