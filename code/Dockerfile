FROM python:3.9

# Copier tous les fichiers du dossier app/ dans le conteneur à l'emplacement /app
COPY . /app
# le premier app correspond au dossier alors que le deuxième correspond au fichier app.py

# Définir le répertoire de travail sur /app
WORKDIR /app
# le /app correspond au dossier dans Docker
# Installer les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Exposer le port spécifié par la variable d'environnement PORT
EXPOSE $PORT

# Lancer l'application Flask avec Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
