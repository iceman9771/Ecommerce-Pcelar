from django.shortcuts import render
from .models import Edukacija
from django.views.generic import ListView, DetailView
from django.http import Http404

class EdukacijaListView(ListView):
	#queryset = Product.objects.all()
	template_name ="edukacija/list.html"

	
	def get_context_data(self,*args,**kwargs):
		context = super(EdukacijaListView, self).get_context_data(*args, **kwargs)
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Edukacija.objects.all()


class EdukacijaDetailView(DetailView):
	template_name ="edukacija/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(EdukacijaDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request =self.request
		pk = self.kwargs.get('pk')
		instance = Edukacija.objects.get_by_id(pk)
		if instance is None:
			raise Http404('instance doesnt exist')
		return instance


def product_detail_view(request, pk=None, *args, **kwargs):
	

	instance = Edukacija.objects.get_by_id(pk)
	if instance is None:
		raise Http404('edukacija doesnt exist')
	
	context = {
		"object" : instance
	}
	return render(request, "edukacija/detail.html", context)


class EdukacijaDetailSlugView(DetailView):
	queryset = Edukacija.objects.all()
	template_name ="edukacija/detail.html"

	def get_context_data(self,*args,**kwargs):
		context = super(EdukacijaDetailSlugView, self).get_context_data(*args, **kwargs)
		return context

	def get_object(self, *args, **kwargs):
		request =self.request
		slug = self.kwargs.get('slug')
		try:
			instance= Edukacija.objects.get(slug=slug ,active=True)
		except Edukacija.DoesNotExist:
			raise Http404("Not Found..")
		except Edukacija.MultipleObjectsReturned:
			qs= Edukacija.objects.filter(slug=slug, active=True)
			instance= qs.first()
		except:
			raise Http404("uhh")

		return instance