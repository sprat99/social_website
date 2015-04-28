# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'account_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=18)),
        ))
        db.send_create_signal(u'account', ['User'])

        # Adding model 'User_Info'
        db.create_table(u'account_user_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.User'], unique=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='male', max_length=6)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('profile', self.gf('django.db.models.fields.CharField')(max_length=240)),
        ))
        db.send_create_signal(u'account', ['User_Info'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'account_user')

        # Deleting model 'User_Info'
        db.delete_table(u'account_user_info')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'account.user_info': {
            'Meta': {'object_name': 'User_Info'},
            'email': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.User']", 'unique': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['account']