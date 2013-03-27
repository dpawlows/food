# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nation'
        db.create_table('food_nation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('food', ['Nation'])

        # Adding model 'Ingredient'
        db.create_table('food_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('food', ['Ingredient'])

        # Adding model 'Recipe'
        db.create_table('food_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Nation'])),
        ))
        db.send_create_signal('food', ['Recipe'])

        # Adding model 'RecipeHasIngredient'
        db.create_table('food_recipehasingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Recipe'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Ingredient'], null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.CharField')(max_length=24, null=True, blank=True)),
        ))
        db.send_create_signal('food', ['RecipeHasIngredient'])


    def backwards(self, orm):
        # Deleting model 'Nation'
        db.delete_table('food_nation')

        # Deleting model 'Ingredient'
        db.delete_table('food_ingredient')

        # Deleting model 'Recipe'
        db.delete_table('food_recipe')

        # Deleting model 'RecipeHasIngredient'
        db.delete_table('food_recipehasingredient')


    models = {
        'food.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'food.nation': {
            'Meta': {'object_name': 'Nation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'food.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['food.Ingredient']", 'through': "orm['food.RecipeHasIngredient']", 'symmetrical': 'False'}),
            'nation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Nation']"})
        },
        'food.recipehasingredient': {
            'Meta': {'object_name': 'RecipeHasIngredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Recipe']"})
        }
    }

    complete_apps = ['food']