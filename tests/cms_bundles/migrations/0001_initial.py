# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 00:36
from __future__ import unicode_literals

from .. import models as cms_bundles_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import scarlet.cms.fields
import scarlet.versioning.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_save', models.DateTimeField(editable=False)),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('vid', models.PositiveIntegerField(editable=False, unique=True)),
                ('object_id', models.PositiveIntegerField(editable=False)),
                ('category', models.CharField(max_length=150)),
                ('slug', models.SlugField(editable=False, max_length=150)),
            ],
            options={
                b'db_table': 'cms_bundles_category_base',
                'managed': False,
            },
            bases=(models.Model, cms_bundles_models.CategoryReferences),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_save', models.DateTimeField(editable=False)),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('vid', models.PositiveIntegerField(editable=False, unique=True)),
                ('object_id', models.PositiveIntegerField(editable=False)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                b'db_table': 'cms_bundles_comment_base',
                'managed': False,
            },
            bases=(models.Model, cms_bundles_models.CommentReferences),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_save', models.DateTimeField(editable=False)),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('vid', models.PositiveIntegerField(editable=False, unique=True)),
                ('object_id', models.PositiveIntegerField(editable=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('body', models.TextField()),
                ('keywords', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                b'db_table': 'cms_bundles_post_base',
                'managed': False,
            },
            bases=(models.Model, cms_bundles_models.PostReferences),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category_version',
            fields=[
                ('last_save', models.DateTimeField(editable=False)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('category', models.CharField(max_length=150)),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_version', to='cms_bundles.Category_base')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model, cms_bundles_models.CategoryVersionReferences),
        ),
        migrations.CreateModel(
            name='Comment_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment_version',
            fields=[
                ('last_save', models.DateTimeField(editable=False)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_version', to='cms_bundles.Comment_base')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_bundles.Post')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model, cms_bundles_models.CommentVersionReferences),
        ),
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('v_last_save', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post_version',
            fields=[
                ('last_save', models.DateTimeField(editable=False)),
                ('state', models.CharField(choices=[(b'published', b'published'), (b'scheduled', b'scheduled'), (b'draft', b'draft'), (b'archived', b'archived')], editable=False, max_length=50)),
                ('last_scheduled', models.DateTimeField(editable=False, null=True)),
                ('date_published', models.DateTimeField(editable=False, null=True)),
                ('user_published', models.CharField(editable=False, max_length=255, null=True)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('body', models.TextField()),
                ('keywords', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms_bundles.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_bundles.Category')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_version', to='cms_bundles.Post_base')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model, cms_bundles_models.PostVersionReferences),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_save', models.DateTimeField(editable=False)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('order', scarlet.cms.fields.OrderField(db_index=True, default=0)),
                ('post', scarlet.versioning.fields.FKToVersion(on_delete=django.db.models.deletion.CASCADE, to='cms_bundles.Post_version')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
        ),
        migrations.AddField(
            model_name='post_version',
            name='tags',
            field=scarlet.versioning.fields.M2MFromVersion(blank=True, to='cms_bundles.Tag'),
        ),
    ]