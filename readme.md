Bien sûr, voici le contenu complet dans un fichier Markdown unique (`voting_app_instructions.md`) :

```markdown
# Application de Vote

Ce projet contient deux applications Flask pour gérer l'écriture et la lecture de votes, ainsi qu'une base de données MySQL pour stocker les votes.

## Configuration Requise

- Docker
- Docker Compose

## Déploiement

1. Clonez ce référentiel sur votre machine locale :

```
git clone https://github.com/votre-utilisateur/application-vote.git
```

2. Accédez au répertoire du projet :

```
cd application-vote
```

3. Lancez les applications à l'aide de Docker Compose :

```
docker-compose up --build
```

Cela va construire les images Docker et démarrer les conteneurs pour les applications d'écriture, de lecture et la base de données MySQL.

4. Accédez aux applications depuis votre navigateur web :

- Application d'écriture : [http://localhost:5000](http://localhost:5000)
- Application de lecture : [http://localhost:5001](http://localhost:5001)

## Arrêt

Pour arrêter les applications, appuyez sur `Ctrl + C` dans le terminal où vous avez lancé `docker-compose up`. Ensuite, vous pouvez exécuter la commande suivante pour supprimer les conteneurs :

```
docker-compose down
```

## Contact

Pour toute question ou assistance, veuillez contacter [votre-email@example.com](mailto:votre-email@example.com).
```

