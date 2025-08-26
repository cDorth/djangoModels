from django.db import models

class Especialidade(models.Model):
    id_especialidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=50, unique=True)
    especialidade = models.ForeignKey(Especialidade,on_delete=models.CASCADE,related_name="medicos"
    )

    def __str__(self):
        return f"{self.nome} - {self.crm}"
