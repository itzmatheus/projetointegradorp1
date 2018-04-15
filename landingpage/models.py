from django.db import models

class Mensagem(models.Model):
	name = models.CharField(verbose_name="Nome completo", max_length=50, blank=True, Null=True)	
	title = models.CharField(verbose_name="Titulo da mensagem", max_length=30)