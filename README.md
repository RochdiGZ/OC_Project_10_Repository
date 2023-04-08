### `Repository name : OC_Project_10_Repository`
### 📖 Vue d'ensemble
Développer une API sécurisée en utilisant Django REST et une base de données `sqlite3`, 
qui permet aux utilisateurs de :
- remonter et suivre des problèmes techniques liés aux projets des entreprises clientes

### 💿 Installer Python
### ⚙️ Cloner depuis GitHub le projet Django
```bash
git clone https://github.com/RochdiGZ/OC_Project_10_Repository.git
```
### ⚙️ Modifier les propriétés du dossier OC_Project_10_Repository comme source de données
-  A l'aide de PyCharm, il suffit de sélectionner le dossier et d'utiliser le bouton droit de la souris pour choisir 
`Mark Directory as > Sources Root`
### 💿 Créer et activer un nouvel environnement virtuel `ENV` & Choisir l'interpréteur Python
```bash
cd OC_Project_10_Repository
```
```bash
python -m venv ENV
```
```bash
ENV/Scripts/activate
```
### ⚙️ Choisir un interpréteur Python depuis le nouvel environnement virtuel
### 💿 Installer tous les modules du projet Django
```bash
python.exe -m pip install --upgrade pip
``` 
```bash
pip install -r requirements.txt
```
### ⚙️ Créer le dossier flake8_report
```bash
flake8 --format=html --htmldir=flake8_report --max-line-length=119
```
### ⚙️ Créer les migrations de tous les modèles du projet
```bash
python manage.py makemigrations
``` 
### ⚙️ Appliquer toutes les migrations
```bash
python manage.py migrate
``` 
### ⚙️ Créer un super utilisateur pour se connecter à partir de l'interface de l'administration Django
```bash
python.exe manage.py createsuperuser
``` 
Dans l'étape suivante, il suffit de rester dans le terminal pour taper un nom d'utilisateur (email) et un mot de passe 
avec confirmation du mot de passe. Par exemple, 
- Email: rochdi@gmail.com
- First_name : Rochdi
- Last_name : GUEZGUEZ
- Password: secret@django
### ⚙️ Lancer le serveur de développement
```bash
python.exe manage.py runserver
``` 
Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page ayant l'adresse 
`http://127.0.0.1:8000`
### ⚙️ Se connecter avec l'interface de l'administration Django via `http://127.0.0.1:8000/admin`
- Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page de l'administration 
Django via `http://127.0.0.1:8000/admin`. Pour se connecter, il suffit de taper le nom du super utilisateur 
`rochdi@gmail.com` et le mot de passe `secret@django`, et de cliquer sur le bouton `Connexion`.
- `Une fois connecté, vous pouvez accéder à notre base de données et savoir les noms de tous les utilisateurs inscrits`
### 📖 Information utile
Pour toute information sur les besoins d'exécution de l'application SoftDesk, veuillez me contacter par email :
Rochdi.GUEZGUEZ@Gmail.Com
`Vous pouvez ainsi accéder à la documentation de notre application via :`
https://documenter.getpostman.com/view/26440710/2s93RNyEfy
