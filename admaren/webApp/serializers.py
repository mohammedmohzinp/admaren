from rest_framework import serializers
from .models import Snippet, Tags


class SnippetsDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Snippet
    fields = ['id', 'title', 'sub_title', 'created_user']


class SnipppetsListSerialzer(serializers.ModelSerializer):
  snippet_details = serializers.HyperlinkedIdentityField(view_name='snip:snippet-detail')
  
  class Meta:
    model = Snippet
    fields = ['title', 'sub_title','snippet_details']


class TagsDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tags
    fields = ['id', 'title']