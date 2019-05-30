# ProjetGLA
Informatique L3 - Universite Paris-Sud

## Authors
- XIAN Qiwei
- CHEN Zixi
- CHAI Kelun


## Objectif
We will implement a management system for a hotel

### Premiere Pas
Installez MySQL, puis `CREATE DATABASE hotel;` sous l'utilisateur root.

### Avant Executer
1. Entrez votre nom d'utilisateur (**root** ici) et votre mot de passe MySQL dans `\hotel\settings.py`.
```
# Ligne 79
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotel',
        'USER': 'root',
        'PASSWORD': 'votre mot de passe',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
2. Creer votre compte gestionnaire dans MySQL comme suite:
`INSERT INTO login_gestionnaire VALUES('root','mots de passe');`

### Executer
Sous répertoire hotel, executer dans l'ordre: 
1. `make makemi`
2. `make mi`
3. `make run`

## Utiliser
1. Ouvrez la page suivante dans votre navigateur
`http://127.0.0.1:8000/index`

