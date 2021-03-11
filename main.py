import sys
import argparse
import configparser
import logging
import os.path
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient

""" 
BlobServiceClient: La classe BlobServiceClient vous permet de manipuler les ressources de stockage Azure et les conteneurs blob.
ContainerClient : La classe ContainerClient vous permet de manipuler des conteneurs de stockage Azure et leurs blobs.
BlobClient : La classe BlobClient vous permet de manipuler des blobs de stockage Azure.
"""

def listb(args, containerclient):
    blob_list=containerclient.list_blobs()
    for blob in blob_list:
    
    """ List the blobs in the container :
        Répertoriez les objets Blob dans le conteneur 
        en appelant la méthode list_blobs. Dans ce cas, 
        un seul objet blob a été ajouté au conteneur. 
        Il n’y a donc qu’un objet blob répertorié.
    """
        print(blob.name)


def upload(cible, blobclient):
    with open(cible, "rb") as f:
        blobclient.upload_blob(f)

"""  Charge le fichier texte local dans l’objet Blob en appelant 
la méthode upload_blob."""


# Download the blob to a local file
# Add 'DOWNLOAD' before the .txt extension
#  so you can see both files in the data directory
def download(filename, dl_folder, blobclient):
    with open(os.path.join(dl_folder,filename), "wb") as my_blob:
        blob_data=blobclient.download_blob()
        blob_data.readinto(my_blob)
    """ Téléchargez l’objet Blob créé précédemment en appelant
        la méthode download_blob. L’exemple de code ajoute le suffixe
        « DOWNLOAD » au nom de fichier afin que vous puissiez voir
        les deux fichiers dans votre système de fichiers local.
        fichier texte pour tester si ça marche.
        wb = écrire 
    """

def main(args,config):
    blobclient=BlobServiceClient(
        #Question Romain : définis compte mais pas sécurisé ?
        f"https://{config['storage']['account']}.blob.core.windows.net",
        config["storage"]["key"],
        logging_enable=False)
    containerclient=blobclient.get_container_client(config["storage"]["container"])
    # liaison avec le container
    if args.action=="list":
        """ """
        return listb(args, containerclient)
        #listeb = liste blob
    else:
        if args.action=="upload": 
            #si ok upload
            blobclient=containerclient.get_blob_client(os.path.basename(args.cible))
            # se connecter au blob client et lui envoyer au fichier
            return upload(args.cible, blobclient)
             #si ok downolad 
        elif args.action=="download":
            blobclient=containerclient.get_blob_client(os.path.basename(args.remote))
            #Télécharger fichier
            return download(args.remote, config["general"]["restoredir"], blobclient)
    

if __name__=="__main__":
    parser=argparse.ArgumentParser("Logiciel d'archivage de documents")
    parser.add_argument("-cfg",default="config.cfg",help="chemin du fichier de configuration")
    parser.add_argument("-lvl",default="info",help="niveau de log")
    subparsers=parser.add_subparsers(dest="action",help="type d'operation")
    subparsers.required=True
    
    parser_s=subparsers.add_parser("upload")
    parser_s.add_argument("cible",help="fichier à envoyer")

    parser_r=subparsers.add_parser("download")
    parser_r.add_argument("remote",help="nom du fichier à télécharger")
    parser_r=subparsers.add_parser("list")

    args=parser.parse_args()

    #erreur dans logging.warning : on a la fonction au lieu de l'entier
    loglevels={"debug":logging.DEBUG, "info":logging.INFO, "warning":logging.WARNING, "error":logging.ERROR, "critical":logging.CRITICAL}
    """ """
    print(loglevels[args.lvl.lower()])
    logging.basicConfig(level=loglevels[args.lvl.lower()])

    config=configparser.ConfigParser()
    config.read(args.cfg)

    sys.exit(main(args,config))