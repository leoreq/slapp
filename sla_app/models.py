from django.db import models
from django.contrib.postgres.fields import HStoreField

# Create your models here.

class Company(models.Model):
	name=models.CharField(max_length=30,unique=True)
	service=models.CharField(max_length=30,unique=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return "We are company {} that offers {}".format(self.name, self.service)

	class Meta:
		ordering = ('service','name',)

class Provider(models.Model):
	name=models.CharField(max_length=30,unique=True)
	company = models.ForeignKey(Company)

	def __str__(self):              # __unicode__ on Python 2
		return "I am {} that offers {} services for company {}".format(self.name, self.company.service,self.company.name)

	class Meta:
		ordering = ('company','name',)

class Services(models.Model):
	company = models.ForeignKey(Company)## Migrate to deletion...unnecesary field 
	provider= models.ForeignKey(Provider)
	client=models.CharField(max_length=30,unique=True)
	agreement_list=HStoreField()
	status=models.BooleanField(default=False)

	def __str__(self):              # __unicode__ on Python 2
		return "I am ticket that offers {} services from company {} for client {}".format(self.company.service, self.company.name, self.client)

