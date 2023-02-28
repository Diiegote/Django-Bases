from django.urls import path
from . import views


urlpatterns = [
   #le agregamos la propiedad name para ponerle un nombre a las rutas y si en algun momento llegamos a modificar la ruta ("project/") por ("project_nuevo/") todo va a seguir funcionando porque estamos mandando a llamar a las rutas por sus nombres y no por sus urls. Ver el archivo base.html y los redirect de views
   path('',views.index,name="index"),
   path('hello/<str:username>',views.hello,name="hello"),
   path('about/',views.about,name="about"),
   path('project/',views.project,name="projects"),
   path('project/<int:id>',views.project_detail,name="projects_detail"),
   path('tasks/',views.tasks,name="tasks"),
   path('create_task/',views.create_task,name="create_task"),
   path('create_project/',views.create_project,name="create_project"),
   
   ]