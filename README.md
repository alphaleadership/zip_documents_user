zip_documents_user
==============

Description
------------
Le projet "zip_documents_user" est un script Python conçu pour archiver les fichiers de l'utilisateur de Windows en les compressant dans un fichier ZIP. Le script recherche les fichiers ayant certaines extensions spécifiées et d'une taille inférieure à 20 Mo, puis les ajoute à une archive ZIP. En outre, un fichier de journalisation est créé pour enregistrer les détails de l'opération.

Utilisation
-----------
1. Double-cliquez sur le fichier exécutable pour lancer le script.
2. Le script parcourt les dossiers de l'utilisateur de Windows et crée une archive ZIP contenant les fichiers correspondant aux extensions spécifiées.
3. Un fichier de journalisation, nommé `nom_du_fichier.log`, est généré pour enregistrer les erreurs rencontrées pendant l'opération.
4. Une fois l'archivage terminé, le fichier ZIP final contenant les fichiers archivés est affiché dans le même répertoire que le fichier exécutable.

Remarque
--------
- Le fichier de journalisation ne contiendra que les erreurs rencontrées pendant l'opération.
- Les fichiers de journalisation sera supprimé après l'archivage.

License
-------
Ce projet est sous licence MIT. Vous pouvez consulter le fichier "LICENSE" pour plus de détails.

Auteur
------
cybersiel
