from django.db import models


class Address(models.Model):
	street		= models.CharField(max_length = 50)
	number		= models.CharField(max_length = 5)
	zip_code	= models.CharField(max_length = 10)
	country		= models.CharField(max_length = 20)

#def __str__(self):
#	return '%s, %s, %s, %s'%(self.street, self.number, self.zip_code, self.country)