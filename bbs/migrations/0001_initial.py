# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Board'
        db.create_table(u'bbs_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('board_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('board_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'bbs', ['Board'])

        # Adding model 'Topic'
        db.create_table(u'bbs_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('topic_content', self.gf('tinymce.models.HTMLField')()),
            ('topic_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('topic_board', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_board', to=orm['bbs.Board'])),
            ('topic_author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_author', to=orm['account.UserProfile'])),
            ('topic_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_specialfield', to=orm['account.SpecialField'])),
            ('topic_tool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_tool', to=orm['account.Tools'])),
            ('topic_final_comment_user', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('topic_final_comment_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('topic_status', self.gf('django.db.models.fields.CharField')(default='normal', max_length=30)),
            ('topic_is_top', self.gf('django.db.models.fields.CharField')(default='no', max_length=30)),
            ('topic_is_pub', self.gf('django.db.models.fields.CharField')(default='no', max_length=30)),
        ))
        db.send_create_signal(u'bbs', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Board'
        db.delete_table(u'bbs_board')

        # Deleting model 'Topic'
        db.delete_table(u'bbs_topic')


    models = {
        u'account.specialfield': {
            'Meta': {'object_name': 'SpecialField'},
            'field_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.tools': {
            'Meta': {'object_name': 'Tools'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tool_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'fav_local': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_specialfield'", 'to': u"orm['account.SpecialField']"}),
            'fav_tool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_tools'", 'to': u"orm['account.Tools']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'bbs.board': {
            'Meta': {'object_name': 'Board'},
            'board_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'board_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bbs.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic_author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_author'", 'to': u"orm['account.UserProfile']"}),
            'topic_board': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_board'", 'to': u"orm['bbs.Board']"}),
            'topic_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_specialfield'", 'to': u"orm['account.SpecialField']"}),
            'topic_content': ('tinymce.models.HTMLField', [], {}),
            'topic_final_comment_time': ('django.db.models.fields.DateTimeField', [], {}),
            'topic_final_comment_user': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topic_is_pub': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '30'}),
            'topic_is_top': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '30'}),
            'topic_status': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '30'}),
            'topic_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'topic_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topic_tool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_tool'", 'to': u"orm['account.Tools']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bbs']