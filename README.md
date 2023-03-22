### `Repository name : OC_Project_10_Repository`
### 📖 Vue d'ensemble
Développer une API sécurisée en utilisant Django REST et une base de données `sqlite3`, 
qui permet aux utilisateurs de :
- remonter et suivre des problèmes techniques liés aux projets des entreprises clientes
- 
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
### ⚙️ Lancer le serveur de développement
```bash
python manage.py runserver
``` 
Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page ayant l'adresse 
`http://127.0.0.1:8000` s'affiche
- `Vous pouvez utiliser le nom du super utilisateur rochdi.guezguez@gmail.com et le mot de pase secret@django` 
pour se connecter à notre application.
### ⚙️ Créer un autre super utilisateur pour se connecter à partir de l'interface de l'administration Django
```bash
python manage.py createsuperuser
``` 
Dans l'étape suivante, il suffit de rester dans le terminal pour taper un nom d'utilisateur et un mot de passe 
avec confirmation du mot de passe.
### ⚙️ Se connecter avec l'interface de l'administration Django via `http://127.0.0.1:8000/admin`
- Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page de l'administration 
Django via `http://127.0.0.1:8000/admin`. Pour se connecter, il suffit de taper le nom d'utilisateur `rochdi.guezguez@gmail.com` et 
le mot de passe `secret@django`, et de cliquer sur le bouton `Connexion`.
- `Une fois connecté, vous pouvez accéder à notre base de données et savoir les noms de tous les utilisateurs inscrits`
- Vous pouvez utiliser un nom d'utilisateur inscrit et le mot de passe `secret@django` 
pour se connecter à notre application.
### 📖 Information utile
Pour toute information sur les besoins d'exécution de l'application LITReview, veuillez me contacter par email :
Rochdi.GUEZGUEZ@Gmail.Com
