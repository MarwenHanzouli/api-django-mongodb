from rest_framework_mongoengine import serializers
from .models import Message, Utilisateur
 
class MessageSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UtilisateurSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

