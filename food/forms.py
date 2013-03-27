from django import forms
from food.models import Recipe,Ingredient
from django.forms import Textarea,TextInput
from django.forms.formsets import formset_factory
from django.core.exceptions import ValidationError
import pdb

class RecipeForm(forms.ModelForm):
	error_css_class="error"
	required_css_class="required"

	ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
	new_ingredient = forms.CharField(max_length=80)
	def __init__(self,*args,**kwargs):
		super(RecipeForm,self).__init__(*args,**kwargs)
#		self.fields['nation'].widget.attrs.update({'class' : 'description'})
		self.fields['nation'].label="Cuisine"
		self.fields['description'].label="Recipe Name"
		#self.fields['new_ingredient'].label="Add Ingredient"


#		self.fields['ingredients'].required = False

	class Meta:
		model = Recipe
#		exclude = ('',)
      

	def clean(self):

		cleaned_data = super(AddForm,self).clean()
		newingredient = cleaned_data.get('new_ingredient')
		ingredient, created = Ingredient.objects.get_or_create(
			description=newingredient)

		return self.cleaned_data
#		if Recipe.objects.filter(ingredients__description=new_ingredient).count() < 1:


		#new_ingredient = self.cleaned_data.get('new_ingredient')

class IngredientForm(forms.ModelForm):
	class Meta:
		model = Ingredient

