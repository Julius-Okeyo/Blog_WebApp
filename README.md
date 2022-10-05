## STEPS IN SUMMARY
### INITIAL SETUP
#### 1. Create a folder.
cd root/  
mkdir {folder name}
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
#### 8. Create a database model.
example:  
#blog/models.py  
from django.db import models  
from django.urls import reverse  

#Post is a subclass of models.Model  
class Post(models.Model):  
    #The class declares the database columns necessary  
    title = models.CharField(max_length=200)  
    author = models.ForeignKey(  
            "auth.User",  
            on_delete=models.CASCADE,  
            )  
    body = models.TextField()  
    def __str__(self):  
        return self.title  
    def get_absolute_url(self):  
        return reverse("post_detail", kwargs={"pk": self.pk})  

#### Create a migration file and migrate database model created. 
python manage.py makemigrations  
python manage.py migrate  
#### Create superadmins.
python manage.py createsuperadmin  
Update {app name}/admin.py.  
example:  
#blog/admin.py  
from django.contrib import admin  
#import our subclass of models.Model   
from .models import Post  
#Register the subclass  
admin.site.register(Post)  
#### URLS
Create {app name}/urls.py  
Configure django_project/urls.py and {app_name}/urls.py  
django_project/urls.py points to {app name}/urls.py which then
points to {app name}/views.py.  
example:  
#blog/urls.py  
from django.urls import path  
#import views existing in the same folder.  
from .views import BlogListView  
urlpatterns = [path("", BlogListView.as_view(), name="home"),]  
#django_project/urls.py  
from django.contrib import admin  
from django.urls import path, include  
urlpatterns = [path("admin/", admin.site.urls),path("", include("blog.urls")),]  
