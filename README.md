## STEPS IN SUMMARY
### INITIAL SETUP
#### 1. Create a folder.
cd root/  
mkdir {folder name}\
#### 2. Create a virtual environment.
cd {created folder}
python -m venv .venv
.venv\Scripts\Activate.ps1
#### 3. Install the correct django version.
python -m pip install django~=4.0.0
#### 4. Start a django project.
django-admin startproject django_project .
~ The dot (.) after project name is important to maintain a neat
directory tree. Without the dot creates a folder called django_project
within another folder called django_project.
~ The name of the project is very important. Once spinned, django
edits several files automatically inserting the project name. It is
recomended that the project be named django_project to avoid future
complications.
#### 5. Create an app.
python manage.py startapp {app name}
#### 6. Edited django_project/settings.py to register the new app.
"{app name}.apps.{app name}Config",
Open django_project/settings.py in text editor and insert path to
new app's Config class accessible through {app name}/apps.py.
#### 7. Perform migration to create database.
python manage.py migrate
