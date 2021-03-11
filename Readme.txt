#debug, info, warning

- Créer un compte de StorageV2 (v2 à usage général) dans le groupe de ressources brief blob 1 
   options de sécurité appropriées : privé
   
- pip install azure-storage-blob

1) Changer le code du document "main.py" pour valider sa compatibilité :
Entrez le nom de votre fichier ".ini" à la place de config.ini ligne 105 :
parser.add_argument("-cfg",default="config.ini",help="chemin du fichier de configuration")


2) changer le code du document "config.ini" pour valider sa compatibilité :

- ouvrir le fichier config.ini 
- restoredir=C:Mettre le chemin du document "download" exemple : \Users\utilisateur\Desktop\downloadtelecharger
account= Mettre le nom de votre ressource  exemple : sarahtruffert
container= Mettre le nom de votre container exemple : conteneur
key= rentrer la clef qui se trouve acceuil> compte> clef d'accès> Afficher les clefs 
exemple :tlO46950geNzTAoVP8f8que2BAOCoJkgUV1Rdnm1zF5Dyhek8zzL0wOnLBz1VkURFKePopqk/QSQMw4KVW8fSQ==



Pour envoyer un blob dans le container : 

Ouvrir le terminal : 

python main.py upload "chemin du fichier upload" 
exemple : PS C:\Users\utilisateur\Desktop\blob_deploiement>
        python main.py upload "C:\Users\utilisateur\Desktop\okayupload\hello world.txt"

Pour récupérer un blob du container : python .\main.py download "nom du fichier à downolad"  
exemple : python .\main.py download .\hello_world.txt  
