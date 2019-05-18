import random
import os
from django.db.models import Q
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from project01.utils import unique_slug_generator

def get_filename_ext(filepath):
	base_name =os.path.basename(filepath)
	name, ext =os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):

	new_filename = random.randint(1,15416151215)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename,
	 	final_filename=final_filename
		)
class ProductQuerySet(models.query.QuerySet):
		def search(self, query):
			lookups =(Q(title__icontains=query) | 
				Q(description__icontains=query) |
				Q(tag__title__icontains=query))
			return self.filter(lookups).distinct()

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)



	
	def get_by_id(self, id):
		qs =self.get_queryset().filter(id=id)
		if qs.count() ==1:
			return qs.first()
		return None
	

class Edukacija(models.Model):
	title 			= models.CharField(max_length=120)
	slug			= models.SlugField(blank=True, unique=True)
	description 	= models.TextField()
	image			= models.ImageField(upload_to=upload_image_path,null=True, blank=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	link			= models.URLField(max_length=200,blank=True)
	active 			= models.BooleanField(default=True)

	objects = ProductManager()

	def get_absolute_url(self):
		#return "/products/{slug}/".format(slug=self.slug)
		return reverse("edukacija:detail", kwargs={"slug": self.slug})

	def __str__(self):
		return self.title




