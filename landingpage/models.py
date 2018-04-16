from django.db import models

class Message(models.Model):
	name = models.CharField(verbose_name="Nome completo", max_length=50, blank=True, null=True)	
	email = models.EmailField(verbose_name="Email", max_length=40, blank=True, null=True) 
	title = models.CharField(verbose_name="Titulo da mensagem", max_length=30)
	menssage = models.TextField(verbose_name="Mensagem", max_length=500)
	data_published = models.DateField("Data de publicaçao", auto_now_add=True)

	def __str__(self):
		return self.name