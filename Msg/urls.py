from django.conf.urls import url
from django.urls import path
from rest_framework_mongoengine import routers as merouters
from .views import MessageViewSet,UtilisateurViewSet
from . import views
merouter = merouters.DefaultRouter()
merouter.register(r'messages', MessageViewSet)
merouter.register(r'utilisateurs', UtilisateurViewSet)
urlpatterns = [
    path('accueil/', views.ajouterUtilisateurs),
    path('envoyer/', views.envoiMessage),
    path('messages/<str:pk>', views.supprimerMessage),
    path('utilisateurs/<str:pk>', views.gestion_utilisateur),
    path('connexion/', views.connexion),
    #url(r'^messages/<str:objet>', views.MessageView.as_view()),
]
 
urlpatterns += merouter.urls