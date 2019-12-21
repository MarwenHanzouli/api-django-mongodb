from django.shortcuts import render,redirect
from rest_framework_mongoengine import viewsets as meviewsets
from .serializers import MessageSerializer, UtilisateurSerializer
from .models import Message , Utilisateur
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import pymongo

class MessageViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
class UtilisateurViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    
url = ('https://randomuser.me/api/?results=20')
response = requests.get(url)
data=response.json()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["messagerie"]
mycol = mydb["utilisateur"]
def recherche(ch):
    for x in mycol.find():
        if x['login']['username']==ch:
            return True
    return False
def ajouterUtilisateurs(request):
    for res in data['results']:
        if recherche(res['login']['username'])==False:
            name=res['name']
            login=res['login']
            picture=res['picture']
            email=res['email']
            user=Utilisateur(email=email,login=login,picture=picture,name=name)
            user.save()
            #x =mycol.insert_one(res)
            #print(x.inserted_id)
    return redirect("http://localhost:8000/")

@api_view(['POST'])
def envoiMessage(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def supprimerMessage(request,pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def connexion(request):
    users=[]
    for u in Utilisateur.objects.all():
        #if u.login.username==request.data['username'] and u.login.password==request.data['username']
        utilisateur=u
        users.append(UtilisateurSerializer(utilisateur))
        if request.method == 'POST':
            serializer = UtilisateurSerializer(utilisateur)
            print(serializer.data['login']['username'])
            print(request.data['password'])
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def gestion_utilisateur(request, pk):
    try:
        utilisateur = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UtilisateurSerializer(utilisateur)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UtilisateurSerializer(utilisateur, data=request.data)
        #print(request.data)
        if serializer.is_valid():
            print(request.data['name'])
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        utilisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)