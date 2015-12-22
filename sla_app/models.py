from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.contrib.auth.models import User


# Create your models here.



class Company(models.Model):
	#New User Field relationship has to be migrated in Django
	user = models.OneToOneField(User,on_delete=models.SET_NULL, related_name="company", null=True, blank=True)
	name=models.CharField(max_length=30,unique=True)
	service=models.TextField(max_length=200,unique=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return "We are company {} that offers {}".format(self.name, self.service)

	class Meta:
		ordering = ('service','name',)

class List(models.Model):
	company = models.ForeignKey(Company)

class Item(models.Model):
    text=models.TextField(default='')
    list=models.ForeignKey(List,default=None)
    status=models.BooleanField(default=False)

class Provider(models.Model):
	name=models.CharField(max_length=30,unique=True)
	company = models.ForeignKey(Company)

	def __str__(self):              # __unicode__ on Python 2
		return "I am {} that offers {} services for company {}".format(self.name, self.company.service,self.company.name)

	class Meta:
		ordering = ('company','name',)

class Services(models.Model):
	## Migrate to deletion...unnecesary field :company = models.ForeignKey(Company)
	provider= models.ForeignKey(Provider)
	client=models.CharField(max_length=30,unique=True)
	agreement_list=HStoreField()
	status=models.BooleanField(default=False)

	def __str__(self):              # __unicode__ on Python 2
		return "I am ticket that offers {} services from company {} for client {}".format(self.provider.company.service, self.provider.company.name, self.client)

