from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Banco( models.Model ):
	banco = models.CharField(max_length=50, unique= True)

	class Meta:
		db_table = 'Banco'

	def __unicode__(self):
		return self.banco

		

class Perfil(models.Model):
	user     = models.OneToOneField(User, unique=True)
	telefono = models.CharField(max_length=20)
	avatar   = models.ImageField(upload_to= 'usuarios/static/images/avatars')
	banco    = models.ForeignKey(Banco)
	cuenta   = models.CharField(max_length=50)

	class Meta:
		db_table =  'Perfil'
