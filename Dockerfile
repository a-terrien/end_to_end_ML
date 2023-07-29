# Utiliser l'image de base Python 3.9
FROM python:3.9

# Créer un répertoire dans le conteneur et le définir comme répertoire de travail
WORKDIR /app

# Copier le contenu du dossier local 'app' dans le dossier '/app' du conteneur
COPY . /app

# Installer les dépendances Python à partir du fichier 'requirements.txt'
RUN pip install -r requirements.txt

# Exposer le port 8080 (port par défaut pour les services Render)
EXPOSE 8080

# Lancer l'application en utilisant Uvicorn
CMD python ./app.py
