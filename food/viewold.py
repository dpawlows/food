from django.views.generic import View, TemplateView, FormView
from food import models as M
from django.db.models import Q
from food.forms import RecipeForm,IngredientForm
from django.views.generic.edit import FormView
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django import http
from django.template import Context, RequestContext
from django.core.context_processors import csrf
import pdb

class FoodView(TemplateView):
	template_name = 'food.html'

	# def render(self,request,*args,**kwargs):
	# 	return render_to_response('home.html',context)

	def get(self,request,*args,**kwargs):
	
		context = self.get_context_data(**kwargs)
		nations = M.Nation.objects.all()
		context.update(dict(nations=nations
				))
		
		return self.render_to_response(context)


class NationView(TemplateView):
	template_name = 'nation.html'

	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		nation = M.Nation.objects.get(pk=kwargs['nation_id'])

		context.update(dict(nation=nation,
			recipes=nation.recipe_set.all()
			))

		return self.render_to_response(context)

class RecipeView(TemplateView):
	template_name = 'recipe.html'

	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		recipe = M.Recipe.objects.get(pk=kwargs['recipe_id'])

		context.update(dict(recipe=recipe,
			ingredients=recipe.ingredients.all()
			))

		return self.render_to_response(context)

class AddView(TemplateView):
	template_name = 'new.html'
	IngredientFormSet = modelformset_factory(M.Ingredient)
	def render(self,request,form):

		context = RequestContext(request,{'title':'Add','form':form})
		return render_to_response('add.html',context)

	def post(self,request,*args,**kwargs):

		formset = IngredientFormSet(request.POST)

		pdb.set_trace()
		rform = RecipeForm(request.POST)
		iform = [Ingredientform(request.POST,prefix=str(x),
			instance=Ingredient()) for x in range(0,3)]

		if pform.is_valid() and all([cf.is_valid() for cf in cforms]):
			ni = form.cleaned_data['new_ingredient']
			ingredient = M.Ingredient.objects.filter(
				description=ni)[0]
			#newrecipe = form.save(commit=False)
			newrecipe=M.Recipe.objects.create(
				description=form.cleaned_data['description'],
					nation=form.cleaned_data['nation'])
			rhi = M.RecipeHasIngredient(recipe=newrecipe,	
				ingredient=ingredient,
				quantity='1')

			rhi.save()
		
			context = self.get_context_data(**kwargs)
			context.update(dict(
				newrecipe = newrecipe
				))

			return self.render_to_response(context)
		else:
			return self.render(request,form)

	def get(self,request,*args,**kwargs):
		rform = RecipeForm()
		
		IngredientFormSet = modelformset_factory(M.Ingredient)
		formset = IngredientFormSet()
		return self.render(request,formset)


class NewView(TemplateView):
	template_name='new.html'

	def get(self,request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		recipe = M.Recipe.objects.get(pk=kwargs('recipe_id'))
		#context.update(dict(recipe=recipe
		#	))
		#context = {'title':'Thanks'}
		return self.render_to_response(context)


