# ProjetGLA
Informatique L3 - Universite Paris-Sud

## Authors
- XIAN Qiwei
- CHEN Zixi
- CHAI Kelun


## Objectif
We will implement a management system for a hotel

### Avant Executer
1. Installez MySQL, puis `CREATE DATABASE hotel;` sous l'utilisateur root

2. Entrez votre nom d'utilisateur (**root** ici) et votre mot de passe MySQL dans `\hotel\settings.py`.
```python
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
3. Creer votre compte gestionnaire dans MySQL:<br>
`INSERT INTO login_gestionnaire VALUES('root','mots de passe');`

### Executer
Sous répertoire hotel, executer dans l'ordre: 
1. `make makemi`
2. `make mi`
3. `make run`

## Utilisation - Gestionnaire
1. Ouvrez la page suivante dans votre navigateur<br>
`http://127.0.0.1:8000/index`
2. Le gestionnaire se connecte au interface gestionnaire avec un nom d'utilisateur et un mot de passe préconfigurés.
3. Au-dessus de l’interface se trouvent `ressources`, `clients`, `demandes` et le bouton de se déconnecter.<br>Les informations de ressource seront affichées par défaut. Notez que les données sont vides lorsque vous vous connectez pour la première fois. Vous devez cliquer sur `ajouter` pour ajouter des informations sur les ressources(chambres).
4. **Ressources**<br>
La page de ressources comprend toutes les informations sur la chambre, y compris le numéro de la chambre, le type de chambre, le prix et les détails. Cliquez sur le `consulter` pour accéder à la nouvelle page. Vous pouvez trouver les informations relatives au muble de ressource, modifier les informations relatives, supprimer le ressource et afficher la réservation concerné.<br>
5. **Client**<br>
La page client contient des informations sur le client. Cliquez sur `consulter` pour trouver toutes les réservations de client.<br>
6. **Demandes**<br>
La page de demande gère toutes les réservations. Vous pouvez consulter, accepter et refuser des réservations.

## Utilisation - Utilisateur
1. Ouvrez la page suivante dans votre navigateur<br>
`http://127.0.0.1:8000/index`<br>
2. L'utilisateur clique sur `click here` pour s'enregistrer et se connecter.
3. Au-dessus de l’interface se trouvent `Home`, `votre profile`, `vos demandes` et le bouton de se déconnecter.<br>La page de réservation s'affichera par défaut.<br>**Plan** est utilisé pour ajouter plusieurs réservations.
