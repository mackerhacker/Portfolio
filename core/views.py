from django.shortcuts import render
from .models import *

def index(request):
	ab = About.objects.all()[0]
	python = Skills.objects.all()[0]
	html = Skills.objects.all()[1]
	css = Skills.objects.all()[2]
	aws = Skills.objects.all()[3]
	linux = Skills.objects.all()[4]
	js = Skills.objects.all()[5]
	ed1 = Education.objects.all()[0]
	ed2 = Education.objects.all()[1]
	exp1 = Experience.objects.all()[0]
	exp2 = Experience.objects.all()[1]
	s1 = Service.objects.all()[0]
	s2 = Service.objects.all()[1]
	s3 = Service.objects.all()[2]
	return render(request,'index.html',{'ab' : ab, 'python' : python, 'html' : html, 'css' : css, 'aws' : aws, 'linux' : linux, 'js' : js, 'ed1' : ed1, 'ed2' : ed2, 'exp1' : exp1, 'exp2' : exp2, 's1' : s1, 's2' : s2, 's3' : s3})

# Create your views here.
