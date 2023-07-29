# Utiliser l'image de base Python 3.9
FROM python:3.9.17

# Copier le contenu du dossier local 'app' dans le dossier '/app' du conteneur
COPY . /app

# Créer un répertoire dans le conteneur et le définir comme répertoire de travail
WORKDIR /app

# Installer les dépendances Python à partir du fichier 'requirements.txt'
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposer le port 8080 (port par défaut pour les services Render)
EXPOSE $PORT

# Lancer l'application en utilisant Uvicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
