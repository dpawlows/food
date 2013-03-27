from django.db import models

class Nation(models.Model):
	description = models.CharField(max_length=80)

	def __unicode__(self):
		return '%s' % (self.description)


class Ingredient(models.Model):
	description = models.CharField(max_length=80)

	def __unicode__(self):
		return '%s' % (self.description)

class Recipe(models.Model):
	description = models.CharField(max_length=255)
	nation = models.ForeignKey(Nation)
	ingredients = models.ManyToManyField(Ingredient,through=
		'RecipeHasIngredient')
	

	def __unicode__(self):
		return '%s' % (self.description)

class RecipeHasIngredient(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient,blank=True,null=True)
	quantity = models.CharField(max_length=24,blank=True,null=True)

	def __unicode__(self):
		return '%s' % (self.recipe)


