from django.db import models

# Create your models here.
class Information(models.Model):
	address = models.CharField(max_length = 500)
	area = models.CharField(max_length = 500)
	phone = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 200)

	def __str__(self):
		return self.address


class Contact(models.Model):
	name = models.CharField(max_length = 500)
	email = models.EmailField(max_length = 400,blank = True)
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name

class Feedback(models.Model):
	name = models.CharField(max_length = 500)
	post = models.CharField(max_length=300)
	comments = models.TextField()
	def __str__(self):
		return self.name