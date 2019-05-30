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
Entrez votre nom d'utilisateur (**root** ici) et votre mot de passe MySQL dans `\hotel\settings.py`.
```
# Ligne 79
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotel',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

### Executer
