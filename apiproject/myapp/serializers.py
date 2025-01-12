from rest_framework import serializers
from myapp.models import contact

class contactSerializer(serializers.HyperlinkedModelSerializer):
       owner = serializers.ReadOnlyField(source='owner.username')
       class Meta:
        model = contact
        fields =['email', 'title', 'name','url','owner']