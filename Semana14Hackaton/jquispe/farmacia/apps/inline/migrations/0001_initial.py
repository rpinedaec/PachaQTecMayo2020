# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'todo_list'
        db.create_table(u'formset_test_todo_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'formset_test', ['todo_list'])

        # Adding model 'todo_item'
        db.create_table(u'formset_test_todo_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('list_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formset_test.todo_list'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'formset_test', ['todo_item'])


    def backwards(self, orm):
        # Deleting model 'todo_list'
        db.delete_table(u'formset_test_todo_list')

        # Deleting model 'todo_item'
        db.delete_table(u'formset_test_todo_item')


    models = {
        u'formset_test.todo_item': {
            'Meta': {'object_name': 'todo_item'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['formset_test.todo_list']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'formset_test.todo_list': {
            'Meta': {'object_name': 'todo_list'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['formset_test']