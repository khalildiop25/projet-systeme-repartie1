# 1. On prend une image Python officielle
FROM python:3.11-slim

# 2. Définir le répertoire de travail dans le container
WORKDIR /app

# 3. Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 4. Exposer le port que Flask va utiliser
EXPOSE 5000

# 5. Commande pour démarrer Flask
CMD ["python", "app.py"]
