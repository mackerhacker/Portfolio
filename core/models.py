from django.db import models

# Create your models here.
class About(models.Model):
	name = models.CharField(max_length=50,verbose_name="Your Name")
	age = models.IntegerField(verbose_name="Age")
	dob = models.DateField(verbose_name="Date of Birth")
	mobile = models.CharField(max_length=15,verbose_name="Mobile NUmber")
	email = models.EmailField(max_length=75, verbose_name="Email")
	city = models.CharField(max_length=50, verbose_name="City")
	website = models.CharField(max_length=40,verbose_name="YOur Website")
	degree = models.CharField(max_length=40, verbose_name="Degree")
	profile = models.CharField(max_length=40, verbose_name="YOur Profile Name")
	shortdesc = models.TextField(max_length=200,verbose_name="Description")
	desc = models.TextField(max_length=600,verbose_name="About You")
	pimg = models.ImageField(upload_to="about",verbose_name="Your PRofile picture")

	class Meta:
		db_table = "about"


class Education(models.Model):
	degree = models.CharField(max_length=50,verbose_name="Dregree")
	year = models.CharField(max_length=20,verbose_name="Duration Of degree")
	university = models.CharField(max_length=75,verbose_name="University Name")
	desc = models.TextField(max_length=100,verbose_name="Education Description")

	class Meta:
		db_table = "education"	

class Service(models.Model):
	title = models.CharField(max_length=70,verbose_name="Portfolio Title")
	desc = models.TextField(max_length=500,verbose_name="Portfolio Description")

	class Meta:
		db_table = "services"

class Skills(models.Model):
	tech = models.CharField(max_length=20,verbose_name="Add YOur skill")
	rate = models.IntegerField(verbose_name="Rate YOurself in %")
	desc = models.TextField(max_length=200,verbose_name="Skill Description")

	class Meta:
		db_table = "skills"					

class Experience(models.Model):
	profile = models.CharField(max_length=50,verbose_name="Job Role")
	year = models.CharField(max_length=20,verbose_name="TOtal Experienc")
	company_name = models.CharField(max_length=75,verbose_name="Company Name")
	desc = models.TextField(max_length=200,verbose_name="Expreenience Description")

	class Meta:
		db_table = "experience"
		
