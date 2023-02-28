from django.shortcuts import render,redirect
from django.http import HttpResponse as response #JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask,CreateNewProject
# Create your views here.

def index(request):
   return render(request,"index.html")

def about(request):
   return render(request,"about.html")

#body

def hello(request,username):
   return response(f"<h1 style='color:green;'>Hello {username}</h1>")



#Mostrando todos los datos del Modelo Project

#def project(request):
   #json = list(Project.objects.values())#Para mostrar todos los valores
   #return JsonResponse(json,safe=False) #Necesitas agregar el safe=False para que funcione


# Busqueda por ID del Modelo Task, no es la mas optima porque si no encuentra un ID crashea la pagina

#def tasks(request,id):
 #json = Task.objects.get(id=id) #buscando un id en especifico
  #return response(f"<h1>Tasks: {json.title}<br/> Descripcion: {json.description} <br/> Id: {id}</h1>")
  
  
#Manera optima de buscar y que no crashe la pagina. Usando el objeto get_object_or_404()

#def tasks(request,id):
   #json= get_object_or_404(Task,id=id)
   #return response(f"<h1>Tasks: {json.title}<br/> Descripcion: {json.description} <br/> Id: {id}</h1>")

def project(request):
   project= Project.objects.all()
   return render(request, 'project.html',{"project":project})

def tasks(request):
   tasks= Task.objects.all()
   return render(request, 'task.html',{"tasks":tasks})

def create_task(request):
   #si me estan visitando a traves del metodo GET:
   if request.method == 'GET':
      return render(request,"create_tasks.html",{"form":CreateNewTask})
     #si me estan visitando a traves del metodo POST:
   else:
      Task.objects.create(title=request.POST['title'], description=request.POST['description'],project_id=2)
      return redirect('tasks') #estamos redireccionando a la ruta tasks pero la llamamos por su name y no por su ruta en si.
   
def create_project(request):
   if request.method == 'GET':
      return render(request,"create_project.html",{"form":CreateNewProject})
   else:
      Project.objects.create(name=request.POST['name'])
      return redirect('project')#estamos redireccionando a la ruta project pero la llamamos por su name y no por su ruta en si 
   
   
   
def project_detail(request,id):
   project= get_object_or_404(Project,id=id)
   tasks= Task.objects.filter(project_id=id)
   return render(request,"project_detail.html",{
   "project":project,
   "tasks":tasks
})