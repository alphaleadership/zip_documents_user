import os
import zipfile
import socket
from datetime import datetime

# Liste des noms de dossiers à rechercher
folder_names = {'Documents', 'Pictures', 'Downloads', 'Music', 'Videos', 'Desktop'}

# Liste des extensions de fichiers à rechercher
file_extensions = tuple(['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.jpg', '.jpeg',
                   '.png', '.gif', '.bmp', '.tiff', '.mp3', '.wav', '.mp4', '.avi', '.mkv', '.mov', 
                   '.txt', '.rtf', '.zip', '.rar', '.7z', '.exe', '.dll', '.bat', '.sys', '.ini', 
                   '.html', '.htm', '.css', '.js', '.php', '.sql', '.xml'])

# Ignorer les dossiers temporaires et cachés
ignore_folders = tuple(['AppData', 'temp', 'tmp'])

# Nom de la machine
hostname = socket.gethostname()

# Date et heure actuelles
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Nom du fichier zip
zip_filename = f"{hostname}_{current_time}.zip"

# Nom du script lui-même
script_name = os.path.basename(__file__)

# Chemin complet du fichier zip
zip_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), zip_filename)

# Nom du fichier de journalisation pour l'utilisateur courant
log_filename = f"{hostname}_{current_time}.log"

# Créer un nouveau fichier zip avec une meilleure compression
with zipfile.ZipFile(zip_filepath, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as myzip:
    # Chemin complet du répertoire de l'utilisateur courant
    user_dir = os.path.expanduser('~')

    # Ouvrir le fichier de journalisation avec l'encodage UTF-8
    with open(log_filename, 'w', encoding='utf-8') as logfile:
        # Parcourir le répertoire de l'utilisateur courant
        for foldername, _, filenames in os.walk(user_dir):
            # Ignorer les dossiers spécifiés et les dossiers cachés
            if any(ignore_folder in foldername for ignore_folder in ignore_folders) or os.path.basename(foldername).startswith('.'):
                continue

            # Ignorer le script, le fichier zip lui-même et le fichier de journalisation
            filenames = [filename for filename in filenames if filename not in {script_name, zip_filename, log_filename}]

            # Vérifier si le dossier ou l'un de ses parents est celui recherché
            current_folder = foldername
            while current_folder != user_dir and current_folder != '/':
                if os.path.basename(current_folder) in folder_names:
                    # Ajouter tous les fichiers du dossier à l'archive zip
                    for filename in filenames:
                        # Chemin complet du fichier
                        file_path = os.path.join(foldername, filename)
                        # Vérifier l'extension du fichier
                        if filename.lower().endswith(file_extensions):
                            # Vérifier la taille du fichier
                            try:
                                file_size = os.path.getsize(file_path)
                                if file_size <= 20 * 1024 * 1024:  # 20 Mo en octets
                                    # Ajouter le fichier à l'archive zip
                                    arcname = os.path.relpath(file_path, user_dir)  # Conserver la structure de l'arborescence dans l'archive zip
                                    myzip.write(file_path, arcname=arcname)
                                else:
                                    logfile.write(f"Ignoré en raison de la taille : {file_path}\n")
                            except OSError:
                                logfile.write(f"Erreur lors de la récupération de la taille du fichier : {file_path}\n")
                    # On a trouvé un dossier correspondant, pas besoin de continuer à chercher
                    break

                # Monter d'un niveau dans l'arborescence
                current_folder = os.path.dirname(current_folder)

    # Ajouter le fichier de journalisation au zip
    myzip.write(log_filename, arcname=log_filename)
    # Supprimer le fichier de journalisation individuel
    os.remove(log_filename)

print(f"L'archivage des fichiers est terminé. Les détails sont dans le fichier zip {zip_filename}.")
