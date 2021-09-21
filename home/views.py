from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):

	return render(request,'index.html')



def about(request):

	return render(request,'about.html')


def contact(request):
	views = {}
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		data = Contact.objects.create(
			name = name,
			email = email,
			subject = subject,
			message = message
			)
		data.save()
		views['message'] = "Success" 
	views['infos'] = Information.objects.all()
	return render(request,'contact.html',views)

def portfolio(request):

	return render(request,'portfolio.html')

def price(request):

	return render(request,'price.html')

def services(request):

	return render(request,'services.html')