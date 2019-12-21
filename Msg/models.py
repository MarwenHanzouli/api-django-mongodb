from django.db import models
from django.http import HttpResponse, Http404
# Create your models here.
from mongoengine import Document, EmbeddedDocument,EmbeddedDocumentField, fields 
import datetime
class Utilisateur(Document):
    email=fields.StringField()
    name=fields.DictField()
    login=fields.DictField()
    picture=fields.DictField()
class Message(Document):
    objet = fields.StringField()
    sujet = fields.StringField()
    lu = fields.BooleanField()
    piece = fields.StringField()
    date = fields.DateTimeField(default=datetime.datetime.utcnow)
    idEmetteur = fields.ObjectIdField()
    idRecepteur = fields.ObjectIdField()
    

    


    
    